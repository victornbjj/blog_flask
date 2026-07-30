from http import HTTPStatus

from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from src.extensions import db
from src.models import User
from src.repositories import user_repository as repo

app = Blueprint("auth", __name__, url_prefix="/auth")


@app.route("/register", methods=["POST"])
def register():
    data = request.json

    if repo.get_by_username(data["username"]) is not None:
        return {"message": "Username already exists"}, HTTPStatus.CONFLICT

    if repo.get_by_email(data["email"]) is not None:
        return {"message": "Email already exists"}, HTTPStatus.CONFLICT

    user = User(username=data["username"], email=data["email"])
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return {"message": "User created"}, HTTPStatus.CREATED


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = repo.get_by_username(data["username"])

    if user is None or not user.check_password(data["password"]):
        return {"message": "Invalid credentials"}, HTTPStatus.UNAUTHORIZED

    access_token = create_access_token(identity=str(user.id))
    return {"access_token": access_token}, HTTPStatus.OK