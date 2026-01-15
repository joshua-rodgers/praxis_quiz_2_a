import os
import sqlite3

from flask import current_app, g


def get_db():
    if "praxis_db" not in g:
        db_path = current_app.config["PRAXIS_DB_PATH"]
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        g.praxis_db = sqlite3.connect(db_path)
        g.praxis_db.row_factory = sqlite3.Row
    return g.praxis_db


def query_db(query, args=None, one=False):
    if args is None:
        args = []
    cursor = get_db().execute(query, args)
    results = cursor.fetchall()
    cursor.close()
    return (results[0] if results else None) if one else results


def init_db():
    db = get_db()
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path, "r", encoding="utf-8") as schema_file:
        db.executescript(schema_file.read())
    db.commit()


def close_db(exception=None):
    db = g.pop("praxis_db", None)
    if db is not None:
        db.close()
