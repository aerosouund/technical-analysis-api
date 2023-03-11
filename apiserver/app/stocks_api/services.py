import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.stocks_api.models import Stock
from app.stocks_api.schemas import StockSchema
from sqlalchemy.sql.expression import func


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("stocks-api")


class StockService:
    @staticmethod
    def retrieve(stock_id: string) -> Stock:
        stock = session.query(func.max(Stock.creation_time)).filter(
        Stock.stock_id == stock_id
    )
        return stock

    @staticmethod
    def retrieve_all() -> List[Stock]:
        return db.session.query(Stock).all()