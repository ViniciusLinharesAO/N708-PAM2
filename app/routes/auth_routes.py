from flask import Blueprint, g, jsonify

from app.controllers.auth_controller import (login_user, refresh_token,
                                             register_user)
from app.middleware.auth_middleware import jwt_required

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/register', methods=['POST'])(register_user)
auth_bp.route('/login', methods=['POST'])(login_user)
@auth_bp.route('/refresh', methods=['POST'])
def refresh():
    return refresh_token()

@auth_bp.route('/me', methods=['GET'])
@jwt_required
def me():
    return jsonify({"message": f"Hello user {g.user_id}!"})
