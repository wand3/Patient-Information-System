#!/usr/bin/env python3
"""
Base Model: create a SQLAlchemy model BaseModel
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from uuid import uuid4, UUID

Base = declarative_base()


class BaseModel:
    """
        attributes and functions for BaseModel class
        Attributes:
            * id, integer primary key
            * created_at, datetime
            * updated_at, datetime
    """
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at= Column(DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """
            instantiation of new BaseModel class
        """
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()

    def __set_attributes(self, attr_dict):
        """
            private method: converts attr_dict values to python class attributes
        """
        if 'id' not in attr_dict:
            attr_dict['id'] = str(uuid4())
        if 'created_at' not in attr_dict:
            attr_dict['created_at'] = datetime.utcnow()
        elif not isinstance(attr_dict['created_at'], datetime):
            attr_dict['created_at'] = datetime.strptime(
                attr_dict['created_at'], "%Y-%m-%d %H:%M:%S.%f"
            )
        
        if 'updated_at' not in attr_dict:
            attr_dict['updated_at'] = datetime.utcnow()
        elif not isinstance(attr_dict['updated_at'], datetime):
            attr_dict['updated_at'] = datetime.strptime(
                attr_dict['updated_at'], "%Y-%m-%d %H:%M:%S.%f"
            )

        for attr, val in attr_dict.items():
            setattr(self, attr, val)