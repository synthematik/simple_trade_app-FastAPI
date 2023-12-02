from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Column, JSON, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON, nullable=False)


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    username = Column(JSON, nullable=False)
    password = Column(JSON, nullable=False)
    registered_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    role_id = Column(Integer, ForeignKey("role.id", ondelete='CASCADE'))

