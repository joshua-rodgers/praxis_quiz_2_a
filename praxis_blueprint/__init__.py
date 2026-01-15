import os

from flask import Blueprint

from praxis_blueprint.db import close_db, init_db
from praxis_blueprint.main_routes import main_bp
from praxis_blueprint.quiz_delivery import quiz_delivery_bp
from praxis_blueprint.utils_ai import ensure_context_cache

praxis_bp = Blueprint(
    "praxis_quiz_2",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/praxis_quiz_2/static",
)


@praxis_bp.record_once
def register_config(state):
    base_dir = os.path.dirname(__file__)
    state.app.config.setdefault(
        "PRAXIS_DB_PATH", os.path.join(base_dir, "praxis_data", "praxis.db")
    )
    state.app.teardown_appcontext(close_db)
    with state.app.app_context():
        init_db()
        ensure_context_cache()


praxis_bp.register_blueprint(main_bp)
praxis_bp.register_blueprint(quiz_delivery_bp, url_prefix="/quiz")
