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


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any complex string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    env = os.environ.get('WEBAPP_ENV')
    if env == None:
        raise Exception("Set WEBAPP_ENV first (dev, test, prod)")
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '{}.db').format(os.environ.get('WEBAPP_ENV'))

    """
        handles long term storage of all class instances
    """
    CNC = {
        'Patient': patient.Patient,
        'History': history.History
    }

    """
        handles storage for database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            creates engine self.__engine
        """
        self.__engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

        if os.environ.get('WEBAPP_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
           returns a dictionary of all objects
        """
        obj_dict = {}
        if cls is not None:
            a_query = self.__session.query(Config.CNC[cls])
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
            return obj_dict
        
        for c in Config.CNC.values():
            a_query = self.__session.query(c)
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
        return obj_dict
    
    def new(self, obj):
        """
            adds objects to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
            commits all changes of current database session
        """
        self.__session.commit()

    def rollback_session(self):
        """
            rollsback a session in the event of an exception
        """
        self.__session.rollback()

    def delete(self, obj=None):
        """
            deletes obj from current database session if not None
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def delete_all(self):
        """
           deletes all stored objects, for testing purposes
        """
        for c in Config.CNC.values():
            a_query = self.__session.query(c)
            all_objs = [obj for obj in a_query]
            for obj in range(len(all_objs)):
                to_delete = all_objs.pop(0)
                to_delete.delete()
        self.save()

    def reload(self):
        """
           creates all tables in database & session from engine
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """
            calls remove() on private session attribute (self.session)
        """
        self.__session.remove()

    def get(self, cls, id):
        """
            retrieves one object based on class name and id
        """
        if cls and id:
            fetch = "{}.{}".format(cls, id)
            all_obj = self.all(cls)
            return all_obj.get(fetch)
        return None

    def count(self, cls=None):
        """
            returns the count of all objects in storage
        """
        return (len(self.all(cls)))


class DevConfig(Config):
    DEBUG = True
    

class TestConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig}
