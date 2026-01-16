import json
import re
from html import escape


def _validate_question_schema(question):
    required_fields = {"question_text", "options", "correct_option"}
    missing = required_fields.difference(question.keys())
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(sorted(missing))}")
    if not isinstance(question["options"], dict) or not question["options"]:
        raise ValueError("Options must be a non-empty object.")
    if question["correct_option"] not in question["options"]:
        raise ValueError("Correct option must exist in options.")


class ContentParser:
    @staticmethod
    def parse_questions(raw_json):
        data = json.loads(raw_json)
        if not isinstance(data, list):
            raise ValueError("Expected a JSON list of questions.")
        for question in data:
            if not isinstance(question, dict):
                raise ValueError("Each question must be an object.")
            _validate_question_schema(question)
        return data

    @staticmethod
    def markdown_to_html(text):
        if not text:
            return ""
        try:
            import markdown  # type: ignore

            html = markdown.markdown(text, extensions=["fenced_code", "tables"])

            # Post-process: Convert <pre><code> blocks to praxis format
            # This regex matches <pre><code ...>content</code></pre> blocks
            def replace_code_block(match):
                code_content = match.group(1)
                # Unescape the HTML entities in the code content
                # (markdown library escapes the content)
                return (
                    '<div class="praxis-code-container">'
                    '<pre class="praxis-code-block" data-language="praxis-pseudo">'
                    f'{code_content}'
                    '</pre></div>'
                )

            # Match <pre><code ...>...</code></pre> patterns
            html = re.sub(
                r'<pre><code(?:\s+class="[^"]*")?>([^<]*(?:<(?!/code>)[^<]*)*)</code></pre>',
                replace_code_block,
                html,
                flags=re.DOTALL
            )

            return html
        except ModuleNotFoundError:
            return "<p>" + escape(text).replace("\n", "<br>") + "</p>"

    @staticmethod
    def wrap_code_snippet(code_snippet):
        if not code_snippet:
            return ""
        escaped = escape(code_snippet)
        return (
            "<div class=\"praxis-code-container\">"
            "<pre class=\"praxis-code-block\" data-language=\"praxis-pseudo\">"
            f"{escaped}"
            "</pre></div>"
        )
