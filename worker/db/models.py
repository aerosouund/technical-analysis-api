from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class StockData(Base):
    __tablename__ = 'stock_data'

    id = Column(Integer, primary_key=True)
    stock_id = Column(String)
    name = Column(String)
    price = Column(Integer)
    availability = Column(Integer)
    timestamp = Column(DateTime)