#!/usr/bin/env python3
"""
Patient Model: create a SQLAlchemy model Patient
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Patient(Base):
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
#     establish database relationship
#     history = Column
    doctor = Column(String(100), nullable=True)


    # def __init__(self, )
