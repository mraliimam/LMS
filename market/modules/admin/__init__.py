from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')

from market.modules.admin import routes