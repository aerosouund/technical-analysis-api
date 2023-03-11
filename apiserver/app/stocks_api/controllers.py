from datetime import datetime
from flask import jsonify
import json
from app.stocks_api.models import Stock
from app.stocks_api.schemas import StockSchema
from app.stocks_api.services import StockService
from flask import request, g
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("Stocks", description="Technical analysis for stocks")


@api.route("/stocks")
class StockResource(Resource):
    def get(self):
        stocks=StockService.retrieve_all()
        stocks=[stock.pop('timestamp', None) for stock in stocks]
        return stocks


@api.route("/stocks/<stock_name>", methods=['GET'])
@api.param("stock_name", "Unique ID for a given stock")
class StockResource(Resource):
    def get(self, stock_name):
        stock=StockService.retrieve(stock_name)
        if stock is None:
            return {"message": "Stock not found"}, 404
        stock.pop('timestamp', None)
        return stock