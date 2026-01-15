import json
from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from praxis_blueprint.db import get_db
from praxis_blueprint.quiz_delivery.content_parser import ContentParser
from praxis_blueprint.utils_ai import generate_questions

main_bp = Blueprint("praxis_main", __name__)


@main_bp.route("/")
def dashboard():
    return render_template("praxis_quiz_2/dashboard.html")


@main_bp.route("/builder", methods=["GET", "POST"])
def builder():
    form_data = {
        "category": "Algorithms & Computational Thinking",
        "difficulty": "Medium",
        "question_count": 5,
        "timer": True,
    }
    error = None
    if request.method == "POST":
        category = request.form.get("category", "").strip()
        difficulty = request.form.get("difficulty", "Medium")
        question_count = request.form.get("question_count", "5")
        timer_enabled = bool(request.form.get("timer"))
        form_data.update(
            {
                "category": category,
                "difficulty": difficulty,
                "question_count": question_count,
                "timer": timer_enabled,
            }
        )
        try:
            count = max(1, min(10, int(question_count)))
        except ValueError:
            error = "Question count must be a number between 1 and 10."
        if not error and not category:
            error = "Category is required."

        if not error:
            try:
                raw_questions = generate_questions(category, count)
                questions = ContentParser.parse_questions(raw_questions)
            except Exception as exc:
                error = f"Unable to generate questions: {exc}"

        if not error:
            db = get_db()
            settings = json.dumps(
                {
                    "category": category,
                    "difficulty": difficulty,
                    "timer": timer_enabled,
                    "question_count": count,
                }
            )
            # Set started_at to current time when quiz is created
            started_at = datetime.now().isoformat() if timer_enabled else None
            cursor = db.execute(
                "INSERT INTO quizzes (user_id, score, total_questions, settings_json, started_at) "
                "VALUES (?, ?, ?, ?, ?)",
                (None, 0, len(questions), settings, started_at),
            )
            quiz_id = cursor.lastrowid
            for question in questions:
                content_json = json.dumps(
                    {
                        "question_text": question.get("question_text"),
                        "code_snippet": question.get("code_snippet"),
                        "options": question.get("options"),
                    }
                )
                question_cursor = db.execute(
                    "INSERT INTO questions (content_json, correct_answer, explanation_md, category, difficulty, source) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    (
                        content_json,
                        question.get("correct_option"),
                        question.get("explanation"),
                        category,
                        difficulty,
                        "ai_generated",
                    ),
                )
                question_id = question_cursor.lastrowid
                db.execute(
                    "INSERT INTO quiz_attempts (quiz_id, question_id, user_answer, is_correct) "
                    "VALUES (?, ?, ?, ?)",
                    (quiz_id, question_id, None, None),
                )
            db.commit()
            return redirect(
                url_for("praxis_quiz_2.praxis_quiz_delivery.active_quiz", quiz_id=quiz_id)
            )

    return render_template(
        "praxis_quiz_2/builder.html",
        form_data=form_data,
        error=error,
    )
