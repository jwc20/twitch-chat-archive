from flask import render_template

from twa.views.main import bp
from twa.db import get_db
from psycopg2.extras import RealDictCursor


def query_db(query, args=(), one=False):
    conn = get_db()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query, args)
    rv = cursor.fetchall()
    cursor.close()
    return (rv[0] if rv else None) if one else rv


@bp.route('/')
def index():
    # get data from chat_messages table
    query = "SELECT * FROM chat_messages ORDER BY timestamp DESC LIMIT 10;"
    messages = query_db(query)
    return render_template("index.html.jinja2", messages=messages)
