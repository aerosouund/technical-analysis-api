from flask import Flask, jsonify, g
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_redis import Redis
import json

db = SQLAlchemy()
redis = Redis()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Stocks API", version="0.1.0")
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    register_routes(api, app)
    db.init_app(app)
    redis.init_app(app)


    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app