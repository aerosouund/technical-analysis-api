from __future__ import annotations
from datetime import datetime
from app import db  # noqa
from sqlalchemy import BigInteger, Column, Date, DateTime, ForeignKey, Integer, String



class Stock(db.Model):
   __abstract__ = True

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    availability = Column(Integer, nullable=False)
    creation_time = Column(DateTime, nullable=False)


def get_stock_model(ticker):
    tablename = 'stock_%s' % ticker  # dynamic table name
    class_name = 'Stock%s' % ticker  # dynamic class name
    Model = type(class_name, (Log,), {
        '__tablename__': tablename
    })
    return Model
