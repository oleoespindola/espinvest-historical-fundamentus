from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TickerModel(Base):
    __tablename__ = "tickers"
    __table_args__ = {"schema": "tickers"}

    id = Column(type_=String, primary_key=True)
    trade_name = Column(type_=String, nullable=False)
