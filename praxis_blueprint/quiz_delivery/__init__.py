from flask import Blueprint

quiz_delivery_bp = Blueprint("praxis_quiz_delivery", __name__)

from praxis_blueprint.quiz_delivery import delivery_routes  # noqa: E402,F401
