from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    content: Mapped[str] = mapped_column(String(500), nullable=False)


class Comment(db.Model):
    user_from_id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    content: Mapped[str] = mapped_column(String(500), nullable=False)


class Follower(db.Model):
    user_from_id: Mapped[int] = mapped_column(primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))


class Saved(db.Model):
    user_from_id: Mapped[int] = mapped_column(primary_key=True)
    liked: Mapped[str] = mapped_column(ForeignKey("post.id"))
