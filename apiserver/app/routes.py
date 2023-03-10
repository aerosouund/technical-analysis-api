def register_routes(api, app, root="api"):
    from app.stocks_api import register_routes as attach_stocks_api

    attach_stocks_api(api, app)