from sqlalchemy import Integer, String, TIMESTAMP, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operation'

    id = Column(Integer, primary_key=True)
    quantity = Column(String)
    figi = Column(String)
    instrument_type = Column(String, nullable=True)
    date = Column(TIMESTAMP(timezone=True))
    type = Column(String)
