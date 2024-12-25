import psycopg2
from flask import current_app, g

import os
import dotenv


def get_db():
    dotenv.load_dotenv()

    if 'db' not in g:
        g.db = psycopg2.connect(
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            host=current_app.config['DB_HOST'],
            port=current_app.config['DB_PORT'],
            dbname=current_app.config['DB_NAME']
        )

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
