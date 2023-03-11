import os
from typing import List, Type

DB_USERNAME = 'admin'
DB_PASSWORD = 'thndr'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'stocks'

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
        f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}