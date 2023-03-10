from flask import Flask, jsonify, g
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Stocks API", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api, app)
    db.init_app(app)


    @app.before_request
    def before_request():
        pass

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app