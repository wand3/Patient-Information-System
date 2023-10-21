#!/usr/bin/env python3
"""
Patient Model: create a SQLAlchemy model Patient
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from models.base_model import BaseModel, Base


Base = declarative_base()


class Patient(BaseModel, Base):
    """Class Patient: Database table named patients
    Attributes:
    * id, integer primary key
    * fname, non-nullable string
    * lname, non-nullable string
    * oname, nullable string
    * address, non-nullable string
    * email, non-nullable string
    * phone, non-nullable integer
    * history, 
    * doctor, nullable string
    """
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    fname = Column(String(100), nullable=False)
    lname = Column(String(100), nullable=False)
    oname = Column(String(100), nullable=True)
    address = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.Integer, unique=True, nullable=False)
#     establish database relationship
    phistory = db.relationship('History', backref='patients', lazy='dynamic')

    # class initialization of Patient model variables
    def __init__(self, fname, lname, oname, address, email, phone):
        self.fname = fname
        self.lname = lname
        self.oname = oname
        self.address = address
        self.email = email
        self.phone = phone

    def __repr__(self):
       return "<User '{} {} {} Address:{} Email: {}'>".format(self.fname, self.lname, self.oname, self.address, self.email,\
                                                              self.phone)