from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Column, JSON, text
from sqlalchemy.ext.declarative import declarative_base
from fastapi_users.db import SQLAlchemyBaseUserTable


Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    role_id = Column(Integer, ForeignKey("role.id", ondelete='CASCADE'))

