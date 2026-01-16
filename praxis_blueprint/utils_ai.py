import logging
import os
import time
from pathlib import Path

from google import genai
from google.genai import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
CACHE_DISPLAY_NAME = "praxis-context-cache"
MODEL_NAME = "gemini-2.5-pro"
CACHE_TTL_SECONDS = 3600
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2


def _get_client():
    """Get Gemini API client with error handling."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.error("GEMINI_API_KEY environment variable is not set")
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Please set it in your environment variables."
        )

    try:
        client = genai.Client(api_key=api_key)
        logger.debug("Gemini client initialized successfully")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize Gemini client: {e}")
        raise RuntimeError(f"Failed to initialize Gemini API client: {e}")


def _reference_files():
    """Get paths to reference files with validation."""
    base_dir = Path(__file__).resolve().parent / "praxis_data"
    files = {
        "objectives": base_dir / "5652_objectives.md",
        "mcqs": base_dir / "MCQs.md",
        "pseudocode": base_dir / "pseudocode_def.md",
    }

    # Validate all files exist
    missing_files = []
    for name, path in files.items():
        if not path.exists():
            missing_files.append(f"{name} ({path})")
            logger.error(f"Reference file missing: {path}")

    if missing_files:
        raise FileNotFoundError(
            f"Required reference files not found: {', '.join(missing_files)}"
        )

    logger.debug(f"All {len(files)} reference files validated")
    return files


def _upload_reference_files(client):
    """Upload reference files to Gemini with retry logic."""
    files = []
    ref_files = _reference_files()

    for name, path in ref_files.items():
        retry_count = 0
        while retry_count < MAX_RETRIES:
            try:
                logger.info(f"Uploading {name}: {path.name}")
                uploaded_file = client.files.upload(
                    file=str(path),
                    config=types.UploadFileConfig(mime_type="text/markdown")
                )
                files.append(uploaded_file)
                logger.debug(f"Successfully uploaded {name} (URI: {uploaded_file.uri})")
                break
            except Exception as e:
                retry_count += 1
                if retry_count >= MAX_RETRIES:
                    logger.error(f"Failed to upload {name} after {MAX_RETRIES} attempts: {e}")
                    raise RuntimeError(f"Failed to upload reference file {name}: {e}")
                logger.warning(f"Upload attempt {retry_count} failed for {name}, retrying in {RETRY_DELAY_SECONDS}s...")
                time.sleep(RETRY_DELAY_SECONDS)

    return files


def ensure_context_cache():
    """
    Ensure context cache exists, creating it if necessary.
    Returns None if API key is not configured (graceful degradation).
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.warning("GEMINI_API_KEY not set, cache will not be available")
        return None

    try:
        client = _get_client()

        # Check for existing cache
        logger.debug(f"Searching for existing cache: {CACHE_DISPLAY_NAME}")
        for cache in client.caches.list():
            if cache.display_name == CACHE_DISPLAY_NAME:
                logger.info(f"Found existing cache: {cache.name}")
                return cache

        # Cache not found, create new one
        logger.info("No existing cache found, creating new cache")
        uploaded_files = _upload_reference_files(client)

        contents = [
            types.Part.from_uri(file_uri=file.uri, mime_type="text/markdown")
            for file in uploaded_files
        ]

        cache = client.caches.create(
            model=MODEL_NAME,
            config=types.CreateCachedContentConfig(
                contents=contents,
                ttl=f"{CACHE_TTL_SECONDS}s",
                display_name=CACHE_DISPLAY_NAME,
            )
        )
        logger.info(f"Successfully created cache: {cache.name} (TTL: {CACHE_TTL_SECONDS}s)")
        return cache

    except FileNotFoundError as e:
        logger.error(f"Reference files not found: {e}")
        raise
    except RuntimeError as e:
        logger.error(f"Cache initialization failed: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during cache initialization: {e}")
        raise RuntimeError(f"Failed to initialize context cache: {e}")


def _get_cache_name():
    """Get cache name with error handling."""
    try:
        cache = ensure_context_cache()
        return cache.name if cache else None
    except Exception as e:
        logger.warning(f"Cache retrieval failed, proceeding without cache: {e}")
        return None


def _clean_json_response(raw_text):
    """
    Strip markdown code fences and validate response is not empty.
    Raises ValueError if response is invalid.
    """
    if not raw_text or not raw_text.strip():
        logger.error("Gemini returned empty response")
        raise ValueError(
            "Gemini returned empty response. This may indicate:\n"
            "1. API quota exceeded\n"
            "2. Invalid API key\n"
            "3. Service unavailability\n"
            "Please check your API configuration and quota."
        )

    text = raw_text.strip()
    original_length = len(text)

    # Remove markdown code fences if present
    if text.startswith("```"):
        logger.debug("Stripping markdown code fences from response")
        # Split by ``` and take the middle part
        parts = text.split("```")
        if len(parts) >= 3:
            text = parts[1]
            # Remove language identifier if present (e.g., "json")
            if text.startswith("json") or text.startswith("JSON"):
                text = text[4:].strip()
            logger.debug(f"Stripped {original_length - len(text)} characters from response")

    cleaned_text = text.strip()

    if not cleaned_text:
        logger.error("Response became empty after cleaning")
        raise ValueError("Response contained only markdown code fences with no content")

    return cleaned_text


def generate_questions(category, count):
    """
    Generate quiz questions using Gemini API with comprehensive error handling.

    Args:
        category: Question category/topic
        count: Number of questions to generate

    Returns:
        Cleaned JSON string containing questions

    Raises:
        RuntimeError: If API call fails after retries
        ValueError: If response is invalid
    """
    if not category or not category.strip():
        raise ValueError("Category cannot be empty")

    if not isinstance(count, int) or count < 1 or count > 20:
        raise ValueError("Count must be an integer between 1 and 20")

    logger.info(f"Generating {count} questions for category: {category}")

    prompt = (
        "You are an exam author for the PRAXIS 5652 Computer Science test.\n"
        "Context: Use the 5652_objectives.md and pseudocode_def.md files from the cache.\n"
        f"Task: Generate {count} multiple-choice questions on '{category}'.\n"
        "STRICT CODE RULES (Zero Tolerance):\n"
        "1. You MUST use the ← arrow for assignment. NEVER use = for assignment.\n"
        "2. You MUST use specific block terminators: end if, end while, end procedure. Do NOT use braces {}.\n"
        "3. Arrays are 0-indexed.\n"
        "4. Do not output Python, Java, or C++ syntax. Use ONLY the provided pseudocode definition.\n"
        "Output Format: Return a JSON LIST of objects. Do not wrap in markdown code fences. Structure: "
        "[{ \"question_text\": \"...\", \"code_snippet\": \"...\", "
        "\"options\": {\"A\": \"...\", \"B\": \"...\"}, "
        "\"correct_option\": \"A\", \"explanation\": \"...\" }]"
    )

    retry_count = 0
    last_error = None

    while retry_count < MAX_RETRIES:
        try:
            client = _get_client()
            cache_name = _get_cache_name()

            # Base arguments for generate_content
            request_kwargs = {
                "model": MODEL_NAME,
                "contents": prompt,
            }

            # If a cache exists, wrap it in a GenerateContentConfig object
            if cache_name:
                logger.debug(f"Using cached content: {cache_name}")
                request_kwargs["config"] = types.GenerateContentConfig(
                    cached_content=cache_name
                )
            else:
                logger.warning("No cache available, generating without context")

            logger.debug("Sending request to Gemini API")
            response = client.models.generate_content(**request_kwargs)

            cleaned_response = _clean_json_response(response.text)
            logger.info(f"Successfully generated {count} questions ({len(cleaned_response)} characters)")
            return cleaned_response

        except (ValueError, RuntimeError) as e:
            # Don't retry validation errors or configuration errors
            logger.error(f"Non-retryable error: {e}")
            raise
        except Exception as e:
            retry_count += 1
            last_error = e
            if retry_count >= MAX_RETRIES:
                logger.error(f"Failed to generate questions after {MAX_RETRIES} attempts: {e}")
                raise RuntimeError(
                    f"Failed to generate questions after {MAX_RETRIES} attempts. "
                    f"Last error: {e}"
                )
            logger.warning(f"Attempt {retry_count} failed, retrying in {RETRY_DELAY_SECONDS}s: {e}")
            time.sleep(RETRY_DELAY_SECONDS * retry_count)  # Exponential backoff

    raise RuntimeError(f"Failed to generate questions: {last_error}")


def explain_answer(question_json, user_answer):
    """
    Generate explanation for student's answer with error handling.

    Args:
        question_json: JSON string of the question
        user_answer: Student's answer choice

    Returns:
        Explanation text (may contain markdown)

    Raises:
        RuntimeError: If API call fails
    """
    if not question_json:
        raise ValueError("question_json cannot be empty")
    if not user_answer:
        raise ValueError("user_answer cannot be empty")

    logger.info(f"Generating explanation for answer: {user_answer}")

    prompt = (
        "Analyze this student's error.\n"
        f"Question: {question_json}\n"
        f"Student Answer: {user_answer}\n"
        "Task:\n"
        "1. Explain the correct logic (referencing specific lines in the code snippet if present).\n"
        "2. Explain the misconception in the student's answer.\n"
        "3. Generate a follow-up practice question (JSON format) that tests the same concept but with different values or logic."
    )

    try:
        client = _get_client()
        cache_name = _get_cache_name()

        request_args = {"model": MODEL_NAME, "contents": prompt}

        if cache_name:
            logger.debug(f"Using cached content for explanation: {cache_name}")
            request_args["config"] = types.GenerateContentConfig(
                cached_content=cache_name
            )

        logger.debug("Requesting answer explanation from Gemini")
        response = client.models.generate_content(**request_args)

        if not response.text:
            logger.warning("Received empty explanation from Gemini")
            return "Unable to generate explanation at this time."

        logger.info("Successfully generated explanation")
        return response.text

    except Exception as e:
        logger.error(f"Failed to generate explanation: {e}")
        # Return a fallback message instead of raising
        return f"Unable to generate detailed explanation due to an error: {str(e)}"
