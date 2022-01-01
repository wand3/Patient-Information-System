#!/usr/bin/env python3
"""
Patient Model: create a SQLAlchemy model Patient
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from webapp import db

Base = declarative_base()


class Patient(db.Model, Base):
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

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    oname = db.Column(db.String(100), nullable=True)
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


class History(db.Model, Base):
    """Class Patient: Database table named patients
    Attributes:
    * id, integer primary key
    * allergies, string
    * complaint, string
    * occupation, string
    * medication, string
    * filed, datetime
    """
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True)
    allergies = db.Column(db.String(100), default='None')
    complaint = db.Column(db.Text())
    occupation = db.Column(db.String(100), nullable=False)
    medication = db.Column(db.Text(200))
    filed = db.Column(db.DateTime, default=datetime.utcnow())
    patient_id = db.Column(db.Integer(), db.ForeignKey('patients.id'))

    def __init__(self, allergies, complaint, occupation, medication, filed):
        """patient History class initialization
        """
        self.allergies = allergies
        self.complaint = complaint
        self.occupation = occupation
        self.medication = medication
        self.filed = filed

    def __repr__(self):
        return "<{} {} {}>".format(self.allergies, self.complaint, self.filed)
