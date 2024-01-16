#!/usr/bin/python3
"""
Database engine and Config
"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import patient, history


basedir = os.path.abspath(os.path.dirname(__file__))
env = os.environ.get('WEBAPP_ENV')



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any complex string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

 
class DevConfig(Config):
    DEBUG = True
    PIS_ADMIN = os.environ.get('PIS_ADMIN') or "administrator@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '{}.db').format(os.environ.get('WEBAPP_ENV'))

    global engine
    engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, echo=True)
    global db_session
    db_session = scoped_session(sessionmaker(autoflush=False, autocommit=False, bind=engine)) 
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(bind=engine)
    

class TestConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '{}.db').format(os.environ.get('WEBAPP_ENV'))
    
    global engine
    engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, echo=True)
    global db_session
    db_session = scoped_session(sessionmaker(autoflush=False, autocommit=False, bind=engine)) 
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(bind=engine)

class ProdConfig(Config):
    pass


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
    }
