#!/usr/bin/env python3
"""
Patient Model: create a SQLAlchemy model Patient
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from models.base_model import BaseModel, Base


class Patient(Base, BaseModel):
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
    address = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(Integer, nullable=False)
    mob = Column(Integer, nullable=False)
    yob = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    bloodGroup = Column(String(13), nullable=False)
    genotype = Column(String(12), nullable=False)
    history = Column(Text(), nullable=True)
    doctor = Column(String(19), nullable=True)


#     establish database relationship
    from .history import History
    phistory = relationship('History', backref='patients', lazy='dynamic', cascade='delete')

    # class initialization of Patient model variables
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
       return "<User '{} {} {} Address:{} Email: {}'>".format(self.fname, self.lname, self.oname, self.address, self.email,\
                                                              self.phone)
