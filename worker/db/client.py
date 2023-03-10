from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import StockData
import logging

def connect():
    engine = create_engine('mysql://admin:thndr@127.0.0.1:3306/stocks')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def commit_message(message):
    # parse the incoming JSON message
    session = connect()
    stock_id = message['stock_id']
    name = message['name']
    price = message['price']
    availability = message['availability']
    timestamp = message['timestamp']


    # create a StockData object and insert it into the database
    stock_data = StockData(stock_id=stock_id, name=name, price=price, availability=availability, timestamp=timestamp)
    session.add(stock_data)
    session.commit()

    # close the session
    session.close()