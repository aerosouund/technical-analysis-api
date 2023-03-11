import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.stocks_api.models import get_stock_model
from sqlalchemy.sql.expression import func
from sqlalchemy import desc


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("stocks-api")


class StockService:
    @staticmethod
    def retrieve(stock_name):
        stock = db.session.query(get_stock_model(stock_name)).order_by(
        desc(get_stock_model(stock_name).timestamp)).limit(1).one()
        return stock._asdict()

    # @staticmethod
    # def retrieve_all() -> List[Stock]:
    #     return db.session.query(Stock).all()