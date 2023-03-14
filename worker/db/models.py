from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stock(Base):
    ''' An abstract class that functions as a template
    for a table mapping for each stock '''

    __abstract__ = True

    stock_id = Column(String)
    name = Column(String)
    price = Column(Integer)
    availability = Column(Integer)
    timestamp = Column(DateTime, primary_key=True)


def get_stock_model(name):
    ''' Create a table mapping class for a given stock '''
    
    tablename = 'stock_%s' % name  # dynamic table name
    class_name = 'Stock%s' % name  # dynamic class name
    Model = type(class_name, (Stock,), {
        '__tablename__': tablename,
        '__table_args__': {'extend_existing': True}

    })
    return Model