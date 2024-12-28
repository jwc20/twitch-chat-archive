import psycopg2
from flask import current_app, g
import dotenv


def get_db():
    dotenv.load_dotenv()

    if 'db' not in g:
        g.db = psycopg2.connect(
            user=current_app.config['DB_USER'][0],
            password=current_app.config['DB_PASSWORD'][0],
            host=current_app.config['DB_HOST'][0],
            port=current_app.config['DB_PORT'][0],
            dbname=current_app.config['DB_NAME'][0]
        )

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
