from flask import Blueprint

bp = Blueprint('main', __name__)

from twa.views.main import routes