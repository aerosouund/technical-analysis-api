from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import get_stock_model
from sqlalchemy import Column, Integer, String, DateTime, MetaData, Table
from sqlalchemy.inspection import inspect
import logging
import os

DB_USER=os.environ['DB_USER']
DB_PASS=os.environ['DB_PASS']
DB_HOST=os.environ['DB_HOST']
DB_NAME=os.environ['DB_NAME']


def connect():
    engine = create_engine(f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_stock_table(name):
    engine = create_engine(f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}")

    if not inspect(engine).has_table('stock_{}'.format(name).replace(' ', '_')):  # If table don't exist, Create.
        meta = MetaData()
        stock_table = Table(
        'stock_{}'.format(name).replace(' ', '_'), meta, 
        Column('stock_id', String(50)), 
        Column('name', String(10)), 
        Column('price', Integer),
        Column('availability', Integer), 
        Column('timestamp', DateTime, index=True)
        )

        meta.create_all(engine, checkfirst=True)


def commit_message(message):
    # parse the incoming JSON message
    session = connect()
    stock_id = message['stock_id']
    name = message['name']
    price = message['price']
    availability = message['availability']
    timestamp = message['timestamp']


    # create a StockName object and insert it into the database
    create_stock_table(name)
    stock_data = get_stock_model(name.replace(' ', '_'))(stock_id=stock_id, name=name, price=price, availability=availability, timestamp=timestamp)
    session.add(stock_data)
    session.commit()

    # close the session
    session.close()