from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, Boolean, Column, Integer, TIMESTAMP, ForeignKey
from sqlalchemy import Table, JSON
from sqlalchemy.orm import Mapped, mapped_column

from database import Base, metadata


class CommonParams(object):
    id = Column(Integer, primary_key=True)


class Role(Base, CommonParams):
    __tablename__ = 'role'
    role_name = Column(String, unique=True, nullable=False)
    permissions = Column(JSON)


class User(SQLAlchemyBaseUserTable[int], Base, CommonParams):
    __tablename__ = 'user'
    username = Column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(Role.id))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
