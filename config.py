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
env = os.environ.get('WEBAPP_ENV')



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any complex string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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
    

 
class DevConfig(Config):
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '{}.db').format(os.environ.get('WEBAPP_ENV'))

    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=engine)
    
    Base.metadata.create_all(engine)
    

class TestConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
    }
