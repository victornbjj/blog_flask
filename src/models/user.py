import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash

from src.extensions import db


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    email:Mapped[str] = mapped_column(sa.String, nullable=False, unique=True)
    password_hash = mapped_column(sa.String, nullable=False)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="author")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.username!r}, active={self.active!r})"  
    
    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password: str):
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self) -> str:
            return f"User(id={self.id!r}, name={self.username!r}, active={self.active!r})" 