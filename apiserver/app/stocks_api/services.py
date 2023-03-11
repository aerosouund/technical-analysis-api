import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.stocks_api.models import get_stock_model
from app.stocks_api.schemas import StockSchema
from sqlalchemy.sql.expression import func


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("stocks-api")


class StockService:
    @staticmethod
    def retrieve(stock_id):
        stock = session.query(func.max(get_stock_model(stock_id).creation_time)).filter
        return stock

    # @staticmethod
    # def retrieve_all() -> List[Stock]:
    #     return db.session.query(Stock).all()