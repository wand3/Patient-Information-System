import os



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any complex string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config);
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 