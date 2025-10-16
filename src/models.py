from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


class Task(db.Model):
    done: Mapped[bool] = mapped_column(Boolean(), default=False)
    creater_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    asignee_id: Mapped[int] = mapped_column(ForeignKey("user.id"))


class Profile(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    dob: Mapped[datetime] = mapped_column(DateTime(timezone=timezone.utc))
    address: Mapped[str] = mapped_column(String(512))
    phone_number: Mapped[str] = mapped.colum()
