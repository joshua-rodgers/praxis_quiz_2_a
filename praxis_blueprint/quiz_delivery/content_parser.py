import json
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

            return markdown.markdown(text, extensions=["fenced_code", "tables"])
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
