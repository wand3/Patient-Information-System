#!/usr/bin/python3
"""
Database engine and Config
"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models import patient, history


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any complex string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    env = os.environ.get('WEBAPP_ENV')
    if env == None:
        raise Exception("Set WEBAPP_ENV first (dev, test, prod)")
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '{}.db').format(os.environ.get('WEBAPP_ENV'))

    # """
    #     handles long term storage of all class instances
    # """
    # CNC = {
    #     'Patient': patient.Patient,
    #     'History': history.History
    # }

    """
        handles storage for database
    """
    # engine = None
    # __session = None

    # def __init__(self):
        # """
        #     creates engine self.__engine
        # """
    global engine
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(engine)

 
class DevConfig(Config):
    DEBUG = True
    

class TestConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
    }
