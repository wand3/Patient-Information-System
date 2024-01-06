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
    username = Column(String(30), unique=True)
    email = Column


#     establish database relationship
    

    # class initialization of Patient model variables
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
       return "<User '{} {} {} Address:{} Email: {}'>".format(self.fname, self.lname, self.oname, self.address, self.email,\
                                                              self.phone)
