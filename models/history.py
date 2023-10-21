#!/usr/bin/python3
"""
City Class from Models Module
"""
import os
from webapp import db
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class History(BaseModel, Base):
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
        if filed is None:
            self.filed = datetime.utcnow()

    def __repr__(self):
        return "<{} {} {}>".format(self.allergies, self.complaint, self.filed)