from flask import Blueprint

teacher = Blueprint('teacher', __name__, url_prefix='/teacher')

from market.modules.teacher import routes