import logging
from datetime import datetime, timedelta
from sqlalchemy import inspect
from sqlalchemy import exc

from app import db
from app.stocks_api.models import get_stock_model
from sqlalchemy import desc


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("stocks-api")


class StockService:
    @staticmethod
    def retrieve(stock_name):
        try:
            stock = db.session.query(get_stock_model(stock_name)).order_by(
            desc(get_stock_model(stock_name).timestamp)).limit(1).one()
        except exc.SQLAlchemyError:
            return None
        return stock._asdict()

    @staticmethod
    def retrieve_all():
        insp = inspect(db.engine)
        tables = insp.get_table_names()
        stocks = []
        for table in tables:
            stock = db.session.query(get_stock_model(table.replace('stock_', ''))).order_by(
            desc(get_stock_model(table.replace('stock_', '')).timestamp)).limit(1).one()
            stocks.append(stock._asdict())
        return stocks
        