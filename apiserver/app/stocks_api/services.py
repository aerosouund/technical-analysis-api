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
            model = get_stock_model(stock_name)
            stock = db.session.query(model).order_by(
            desc(model.timestamp)).limit(1).one()
        except exc.SQLAlchemyError:
            return None
        return stock._asdict()

    @staticmethod
    def retrieve_all():
        insp = inspect(db.engine)
        tables = insp.get_table_names()
        stocks = []
        for table in tables:
            model = get_stock_model(table.replace('stock_', ''))
            stock = db.session.query(model).order_by(
            desc(model.timestamp)).limit(1).one()
            stocks.append(stock._asdict())
        return stocks
        