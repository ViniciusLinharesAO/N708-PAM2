import os
from datetime import datetime, timedelta, timezone

import jwt
from passlib.hash import bcrypt

from app.core.extensions import db
from app.models.user_model import User


class AuthService:

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hash(password)

    @staticmethod
    def verify_password(password: str, hash: str) -> bool:
        return bcrypt.verify(password, hash)

    @staticmethod
    def create_user(username: str, email: str, password: str):
        password_hash = AuthService.hash_password(password)
        user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def generate_token(user_id: int) -> str:
        payload = {
            'user_id': user_id,
            'exp': datetime.now(timezone.utc) + timedelta(hours=1)
        }
        token = jwt.encode(payload, os.getenv("SECRET_KEY", "secret"), algorithm="HS256")
        return token

    @staticmethod
    def authenticate_user(email: str, password: str):
        user = User.query.filter_by(email=email).first()
        if user and AuthService.verify_password(password, user.password_hash):
            return AuthService.generate_token(user.id)
        return None

    @staticmethod
    def generate_token_pair(user_id: int) -> dict:
        access_payload = {
            'user_id': user_id,
            'exp': datetime.now(timezone.utc) + timedelta(minutes=15),
            'type': 'access'
        }
        refresh_payload = {
            'user_id': user_id,
            'exp': datetime.now(timezone.utc) + timedelta(days=7),
            'type': 'refresh'
        }
        secret = os.getenv("SECRET_KEY", "secret")
        access_token = jwt.encode(access_payload, secret, algorithm="HS256")
        refresh_token = jwt.encode(refresh_payload, secret, algorithm="HS256")
        return {"access_token": access_token, "refresh_token": refresh_token}

    @staticmethod
    def decode_token(token: str):
        try:
            payload = jwt.decode(token, os.getenv("SECRET_KEY", "secret"), algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
