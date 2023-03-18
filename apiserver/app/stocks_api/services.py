import logging
from datetime import datetime, timedelta
from sqlalchemy import inspect
from sqlalchemy import exc
import app
from app import db, redis
from app.stocks_api.models import get_stock_model
from sqlalchemy import desc



class StockService:
    @staticmethod
    def retrieve(stock_name):
        '''Retrieve a specific stock'''

        try:
            # get the stock with the max value in timestamp
            model = get_stock_model(stock_name)
            stock = db.session.query(model).order_by(
            desc(model.timestamp)).limit(1).one()
        except exc.SQLAlchemyError:
            return None
        return stock._asdict()

    @staticmethod
    def retrieve_all():
        '''Retrieve all stocks'''

        # check all tables in the database and get the max timestamp stock in it
        insp = inspect(db.engine)
        tables = insp.get_table_names()
        stocks = []
        for table in tables:
            model = get_stock_model(table.replace('stock_', ''))
            stock = db.session.query(model).order_by(
            desc(model.timestamp)).limit(1).one()
            stocks.append(stock._asdict())
        return stocks


class AnalysisService:
    @staticmethod
    def post_analysis(stock_name, analysis):
        '''Post analysis to Redis'''
        redis.mset({stock_name.replace(' ', '_'): analysis})

    @staticmethod
    def get_analysis(stock_name):
        '''Get analysis from Redis'''
        analysis = redis.get(stock_name)
        return analysis
        