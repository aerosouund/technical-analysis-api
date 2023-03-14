from app.stocks_api.models import Stock
from app.stocks_api.schemas import StockSchema


def register_routes(api, app, root=""):
    from app.stocks_api.controllers import api as stocks_api

    api.add_namespace(stocks_api, path=f"/{root}")