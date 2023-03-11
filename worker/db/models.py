from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stock(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    stock_id = Column(String)
    name = Column(String)
    price = Column(Integer)
    availability = Column(Integer)
    timestamp = Column(DateTime)


def get_stock_model(name):
    tablename = 'stock_%s' % name  # dynamic table name
    class_name = 'Stock%s' % name  # dynamic class name
    Model = type(class_name, (Stock,), {
        '__tablename__': tablename
    })
    return Model