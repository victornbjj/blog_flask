import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.extensions import db


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="author")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.username!r}, active={self.active!r})"