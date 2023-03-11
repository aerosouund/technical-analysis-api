from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import get_stock_model
from sqlalchemy import Column, Integer, String, DateTime, MetaData, Table
from sqlalchemy.inspection import inspect
import logging

def connect():
    engine = create_engine('mysql://admin:thndr@127.0.0.1:3306/stocks')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_stock_table(name):
    engine = create_engine('mysql://admin:thndr@127.0.0.1:3306/stocks')

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


    # create a StockData object and insert it into the database
    create_stock_table(name)
    stock_data = get_stock_model(name.replace(' ', '_'))(stock_id=stock_id, name=name, price=price, availability=availability, timestamp=timestamp)
    session.add(stock_data)
    session.commit()

    # close the session
    session.close()