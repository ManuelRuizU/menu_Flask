# routes/urls.py

from flask import Blueprint
from views.views import index, add_product, register_view, login_view

# Crear Blueprints
main = Blueprint('main', __name__)
auth_bp = Blueprint('auth_bp', __name__)

# Definir rutas y asociarlas con las vistas
main.route('/')(index)
main.route('/add_product', methods=['GET', 'POST'])(add_product)

auth_bp.route('/register', methods=['GET', 'POST'])(register_view)
auth_bp.route('/login', methods=['GET', 'POST'])(login_view)
