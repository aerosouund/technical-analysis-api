import json
from flask import request
from app.stocks_api.services import StockService, AnalysisService
from flask_restx import Namespace, Resource

api = Namespace("Stocks", description="Technical analysis for stocks")


@api.route("/stocks", methods=['GET'])
class StockResource(Resource):
    def get(self):
        stocks=StockService.retrieve_all()
        stocks=[{key : val for key, val in stock.items() if key != 'timestamp'} for stock in stocks]  # remove the timestamp key
        return stocks


@api.route("/stocks/<stock_name>", methods=['GET'])
@api.param("stock_name", "Unique ID for a given stock")
class StockResource(Resource):
    def get(self, stock_name):
        stock=StockService.retrieve(stock_name)
        if stock is None:
            return {"message": "Stock not found"}, 404

        # retrieve technical analysis from Redis and turn it into JSON
        try: 
            technical_analysis = json.loads(AnalysisService.get_analysis(stock_name).decode('UTF-8'))
            stock['technical_analysis'] = technical_analysis  # remove the timestamp key
        except AttributeError: # handle the case of no analysis posted for that stock
            pass
        stock.pop('timestamp', None)
        return stock


@api.route("/admin/stocks/<stock_name>/analysis", methods=['POST'])
@api.param("stock_name", "Unique ID for a given stock")
class AnalysisResource(Resource):
    def post(self, stock_name):
        analysis = request.json
        if sorted(list(analysis.keys())) != sorted(['target', 'type']):
            return {"message": "Invalid payload"}, 404
            
        stock=StockService.retrieve(stock_name)
        if stock is None:
            return {"message": "Stock not found"}, 404

        # Compute target hit with a comparison with the current price
        analysis['target_hit'] = analysis["target"] >= stock["price"] and analysis["type"] == "UP" or analysis["target"] < stock["price"] and analysis["type"] == "DOWN"

        AnalysisService.post_analysis(stock_name, json.dumps(analysis))
        return analysis