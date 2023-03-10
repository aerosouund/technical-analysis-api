from datetime import datetime

from app.stocks_api.models import Stock
from app.stocks_api.schemas import StockSchema
from app.stocks_api.services import StockService
from flask import request, g
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("Stocks", description="Technical analysis for stocks")


@api.route("/stocks")
class StockResource(Resource):
    @responds(schema=StockSchema, many=True)
    def get(self) -> List[Stock]:
        stocks: List[Stock] = StockService.retrieve_all()
        return stocks


@api.route("/stocks/<stock_id>")
@api.param("person_id", "Unique ID for a given stock", _in="query")
class StockResource(Resource):
    @responds(schema=StockSchema)
    def get(self, stock_id) -> Stock:
        stock: Stock = StockService.retrieve(stock_id)
        return stock