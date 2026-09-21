from sqlalchemy import Column, String, Double, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FundamentusModel(Base):
    __tablename__ = "fundamentus"
    __table_args__ = {"schema": "tickers"}

    id = Column(type_=Integer, primary_key=True)
    ticker_id = Column(type_=String, unique=True, index=True)
    price = Column(type_=Double)
    pe_ratio = Column(type_=Double)
    pb_ratio = Column(type_=Double)
    ps_ratio = Column(type_=Double)
    dividend_yield = Column(type_=Double)
    price_to_assets = Column(type_=Double)
    price_to_working_capital = Column(type_=Double)
    price_to_ebit = Column(type_=Double)
    price_to_net_current_assets = Column(type_=Double)
    ev_to_ebit = Column(type_=Double)
    ev_to_ebitda = Column(type_=Double)
    gross_margin = Column(type_=Double)
    ebit_margin = Column(type_=Double)
    net_margin = Column(type_=Double)
    current_ratio = Column(type_=Double)
    roic = Column(type_=Double)
    roe = Column(type_=Double)
    average_daily_volume_2m = Column(type_=Double)
    net_worth = Column(type_=Double)
    net_debt_to_equity = Column(type_=Double)
    revenue_growth_5y = Column(type_=Double)
