from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import stock_data

def connect():
    engine = create_engine('postgresql://your_username:your_password@localhost/your_database_name')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def commit_message(message):
    # parse the incoming JSON message
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