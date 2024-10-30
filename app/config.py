import os

from flask.config import Config
from dotenv import load_dotenv
load_dotenv()

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True
    TESTING = True

