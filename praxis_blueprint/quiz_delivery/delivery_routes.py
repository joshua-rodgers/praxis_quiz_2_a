import json
from datetime import datetime

from flask import abort, jsonify, render_template, request

from praxis_blueprint.db import get_db, query_db
from praxis_blueprint.quiz_delivery.content_parser import ContentParser

from praxis_blueprint.quiz_delivery import quiz_delivery_bp


@quiz_delivery_bp.route("/active/<int:quiz_id>")
def active_quiz(quiz_id):
    quiz = query_db("SELECT * FROM quizzes WHERE id = ?", [quiz_id], one=True)
    if quiz is None:
        abort(404)
    attempts = query_db(
        "SELECT q.id as question_id, q.content_json "
        "FROM quiz_attempts qa "
        "JOIN questions q ON qa.question_id = q.id "
        "WHERE qa.quiz_id = ? "
        "ORDER BY qa.id ASC",
        [quiz_id],
    )
    questions = []
    for attempt in attempts:
        content = json.loads(attempt["content_json"])
        questions.append(
            {
                "id": attempt["question_id"],
                "question_text": content.get("question_text", ""),
                "code_snippet": content.get("code_snippet", ""),
                "options": content.get("options", {}),
            }
        )
    settings = json.loads(quiz["settings_json"] or "{}")
    timer_seconds = 0

    if settings.get("timer"):
        # If timer is enabled, calculate remaining time based on started_at
        total_timer_seconds = 300  # 5 minutes

        if quiz["started_at"]:
            try:
                # Parse the started_at timestamp
                started_at = datetime.fromisoformat(quiz["started_at"])
                elapsed_seconds = int((datetime.now() - started_at).total_seconds())
                timer_seconds = max(0, total_timer_seconds - elapsed_seconds)
            except (ValueError, TypeError):
                # If parsing fails, use full timer
                timer_seconds = total_timer_seconds
        else:
            # No started_at, use full timer
            timer_seconds = total_timer_seconds

    return render_template(
        "praxis_quiz_2/quiz/active_quiz.html",
        quiz={"id": quiz["id"], "timer_seconds": timer_seconds},
        questions=questions,
    )


@quiz_delivery_bp.route("/submit", methods=["POST"])
def submit_answer():
    payload = request.get_json(silent=True) or {}
    quiz_id = payload.get("quiz_id")
    question_id = payload.get("question_id")
    user_answer = payload.get("user_answer")
    if not all([quiz_id, question_id, user_answer]):
        return jsonify({"error": "Missing required fields."}), 400

    question = query_db(
        "SELECT correct_answer FROM questions WHERE id = ?",
        [question_id],
        one=True,
    )
    if question is None:
        return jsonify({"error": "Question not found."}), 404

    is_correct = 1 if user_answer == question["correct_answer"] else 0
    db = get_db()
    db.execute(
        "UPDATE quiz_attempts SET user_answer = ?, is_correct = ? "
        "WHERE quiz_id = ? AND question_id = ?",
        (user_answer, is_correct, quiz_id, question_id),
    )
    correct_count = query_db(
        "SELECT COUNT(*) as correct_count FROM quiz_attempts WHERE quiz_id = ? AND is_correct = 1",
        [quiz_id],
        one=True,
    )
    score = correct_count["correct_count"] if correct_count else 0
    db.execute("UPDATE quizzes SET score = ? WHERE id = ?", (score, quiz_id))
    db.commit()
    return jsonify(
        {
            "is_correct": bool(is_correct),
            "correct_answer": question["correct_answer"],
            "score": score,
        }
    )


@quiz_delivery_bp.route("/results/<int:quiz_id>")
def results(quiz_id):
    quiz = query_db("SELECT * FROM quizzes WHERE id = ?", [quiz_id], one=True)
    if quiz is None:
        abort(404)
    attempts = query_db(
        "SELECT q.content_json, q.correct_answer, q.explanation_md, qa.user_answer "
        "FROM quiz_attempts qa "
        "JOIN questions q ON qa.question_id = q.id "
        "WHERE qa.quiz_id = ? "
        "ORDER BY qa.id ASC",
        [quiz_id],
    )
    attempt_data = []
    for attempt in attempts:
        content = json.loads(attempt["content_json"])
        attempt_data.append(
            {
                "question_text": content.get("question_text", ""),
                "code_html": ContentParser.wrap_code_snippet(
                    content.get("code_snippet")
                ),
                "user_answer": attempt["user_answer"],
                "correct_answer": attempt["correct_answer"],
                "explanation_html": ContentParser.markdown_to_html(
                    attempt["explanation_md"]
                ),
            }
        )
    return render_template(
        "praxis_quiz_2/quiz/results.html",
        quiz=quiz,
        attempts=attempt_data,
    )
