import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.stocks_api.models import Stock
from app.stocks_api.schemas import StockSchema

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")


class StockService:

    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        return db.session.query(Person).all()