from flask import render_template

from twa.views.main import bp

@bp.route('/')
def index():
    return render_template("index.html.jinja2")
