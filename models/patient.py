#!/usr/bin/env python3
"""
Patient Model: create a SQLAlchemy model Patient
"""
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from models.base_model import BaseModel, Base


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
    address = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(Integer, unique=True, nullable=False)
    mob = Column(Integer, nullable=False)
    yob = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    bloodGroup = Column(String(3), nullable=False)
    genotype = Column(String(2), nullable=False)
    history = Column(Text())
    doctor = Column(String(), nullable=True)


#     establish database relationship
    phistory = relationship('History', backref='patients', lazy='dynamic', cascade='delete')

    # class initialization of Patient model variables
    def __init__(self, fname, lname, oname, address, email, phone, mob, yob, gender, bloodGroup, genotype, history, doctor):
        self.fname = fname
        self.lname = lname
        self.oname = oname
        self.address = address
        self.email = email
        self.phone = phone
        self.mob = mob
        self.yob = yob
        self.gender = gender
        self.bloodGroup = bloodGroup
        self.genotype = genotype
        self.history = history
        self.doctor = doctor
        super().__init__()


    def __repr__(self):
       return "<User '{} {} {} Address:{} Email: {}'>".format(self.fname, self.lname, self.oname, self.address, self.email,\
                                                              self.phone)
