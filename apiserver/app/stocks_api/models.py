from __future__ import annotations
from datetime import datetime
from app import db
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, inspect



class Stock(db.Model):
    ''' An abstract class that functions as a template
    for a table mapping for each stock '''

    __abstract__ = True

    stock_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    availability = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def _asdict(self):
    # convert the class to dict
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}


def get_stock_model(ticker):
    ''' Create a table mapping class for a given stock '''

    tablename = 'stock_%s' % ticker  # dynamic table name
    class_name = 'Stock%s' % ticker  # dynamic class name
    Model = type(class_name, (Stock,), {
        '__tablename__': tablename,
        '__table_args__': {'extend_existing': True}
    })
    print('loaded model %s' %Model)
    return Model
