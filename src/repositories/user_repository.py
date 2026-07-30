from sqlalchemy import inspect

from src.extensions import db
from src.models import User


def list_all():
    query = db.select(User)
    return db.session.scalars(query).all()


def get_by_email(email: str) -> User | None:
    query = db.select(User).where(User.email == email)
    return db.session.scalar(query)


def get_by_username(username: str) -> User | None:
    query = db.select(User).where(User.username == username)
    return db.session.scalar(query)
    
    
    
def get_by_id_or_404(user_id: int) -> User:
    return db.get_or_404(User, user_id)


def create(username: str) -> User:
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return user


def update(user: User, data: dict) -> User:
    mapper = inspect(User)
    for column in mapper.attrs:
        if column.key in data:
            setattr(user, column.key, data[column.key])

    db.session.commit()
    return user


def delete(user: User) -> None:
    db.session.delete(user)
    db.session.commit()