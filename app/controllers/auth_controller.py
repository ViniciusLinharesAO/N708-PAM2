from flask import jsonify, request
from pydantic import ValidationError

from app.models.user_model import User
from app.schemas.user_schema import UserCreateSchema, UserLoginSchema
from app.services.auth_service import AuthService


def register_user():
    try:
        data = UserCreateSchema(**request.json)
        user = AuthService.create_user(data.username, data.email, data.password)
        return jsonify({"message": "User created", "user_id": user.id}), 201
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def login_user():
    try:
        data = UserLoginSchema(**request.json)
        token = AuthService.authenticate_user(data.email, data.password)
        if token:
            return jsonify({"token": token})
        return jsonify({"error": "Invalid credentials"}), 401
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

def login_user():
    try:
        data = UserLoginSchema(**request.json)
        user = User.query.filter_by(email=data.email).first()
        if user and AuthService.verify_password(data.password, user.password_hash):
            tokens = AuthService.generate_token_pair(user.id)
            return jsonify(tokens)
        return jsonify({"error": "Invalid credentials"}), 401
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

def refresh_token():
    try:
        refresh_token = request.json.get("refresh_token")
        payload = AuthService.decode_token(refresh_token)

        if payload.get("type") != "refresh":
            return jsonify({"error": "Invalid token type"}), 403

        new_tokens = AuthService.generate_token_pair(payload['user_id'])
        return jsonify(new_tokens)
    except Exception as e:
        return jsonify({"error": str(e)}), 401
