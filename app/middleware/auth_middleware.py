from functools import wraps

from flask import g, jsonify, request

from app.services.auth_service import AuthService


def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing token"}), 401

        token = auth_header.split(" ")[1]
        try:
            payload = AuthService.decode_token(token)
            if payload.get("type") != "access":
                return jsonify({"error": "Invalid token type"}), 403
            g.user_id = payload["user_id"]

        except Exception as e:
            return jsonify({"error": str(e)}), 401

        return f(*args, **kwargs)
    return decorated_function
