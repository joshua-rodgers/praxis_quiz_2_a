from flask import Flask

from praxis_blueprint import praxis_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(praxis_bp, url_prefix="/praxis")
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
