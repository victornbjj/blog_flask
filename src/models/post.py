import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.extensions import db


class Post(db.Model):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        sa.DateTime, server_default=sa.func.now()
    )
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"))

    author: Mapped["User"] = relationship(back_populates="posts")

    def __repr__(self) -> str:
        return (
            f"Post(id={self.id!r}, title={self.title!r}, "
            f"author_id={self.author_id!r})"
        )