from __future__ import annotations
from datetime import datetime
from app import db  # noqa
from sqlalchemy import BigInteger, Column, Date, DateTime, ForeignKey, Integer, String



class Stock(db.Model):
    __tablename__ = "stock_data"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    availability = Column(Integer, nullable=False)
    creation_time = Column(DateTime, nullable=False)
