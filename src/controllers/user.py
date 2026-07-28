from http import HTTPStatus

from flask import Blueprint, request

from src.repositories import user_repository as repo

app = Blueprint("user", __name__, url_prefix="/users")


def _serialize(user):
    return {"id": user.id, "username": user.username}


@app.route("/", methods=["GET", "POST"])
def list_or_create_user():
    if request.method == "POST":
        data = request.json
        repo.create(username=data["username"])
        return {"message": "User created"}, HTTPStatus.CREATED
    else:
        users = repo.list_all()
        return {"users": [_serialize(user) for user in users]}, HTTPStatus.OK
        

    

@app.route("/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = repo.get_by_id_or_404(user_id)
    return _serialize(user)


@app.route("/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    user = repo.get_by_id_or_404(user_id)
    updated_user = repo.update(user, request.json)
    return _serialize(updated_user)


@app.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = repo.get_by_id_or_404(user_id)
    repo.delete(user)
    return "", HTTPStatus.NO_CONTENT