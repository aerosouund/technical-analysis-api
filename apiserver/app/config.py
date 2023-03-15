import os
from typing import List, Type

DB_USER=os.environ['DB_USER']
DB_PASS=os.environ['DB_PASS']
DB_HOST=os.environ['DB_HOST']
DB_NAME=os.environ['DB_NAME']

class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "test"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
    )
    REDIS_HOST = os.environ['REDIS_HOST']
    REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
    REDIS_PORT = 6379
    REDIS_DB = 0
    


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}