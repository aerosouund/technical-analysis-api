from datetime import datetime
from app.stocks_api.models import Stock
from flask import request
from app.stocks_api.services import StockService, AnalysisService
from flask_restx import Namespace, Resource

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("Stocks", description="Technical analysis for stocks")


@api.route("/stocks", methods=['GET'])
class StockResource(Resource):
    def get(self):
        stocks=StockService.retrieve_all()
        stocks=[{key : val for key, val in stock.items() if key != 'timestamp'} for stock in stocks]
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


@api.route("/admin/stocks/<stock_name>/analysis", methods=['POST'])
@api.param("stock_name", "Unique ID for a given stock")
class AnalysisResource(Resource):
    def post(self, stock_name):
        stock=StockService.retrieve(stock_name)
        if stock is None:
            return {"message": "Stock not found"}, 404

        analysis = request.json
        analysis['target_hit'] = analysis.target >= stock.price and analysis.type == "UP" |
        analysis.target < stock.price and analysis.type == "DOWN"

        AnalysisService.add(stock_name, analysis)
        return analysis