#!/usr/bin/python3
"""
City Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from patient import Patient
from sqlalchemy import Column, Integer, String, Text, ForeignKey


class History(Base, BaseModel):
    """Class Patient: Database table named patients
    Attributes:
        * id, integer primary key
        * allergies, string
        * complaint, string
        * occupation, string
        * medication, string
    """
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    allergies = Column(String(100), default='None')
    complaint = Column(Text())
    occupation = Column(String(100), nullable=False)
    medication = Column(Text(200))
    patient_id = Column(Integer(), ForeignKey('patients.id'), nullable=False)


    def __init__(self, allergies, complaint, occupation, medication):
        """patient History class initialization
        """
        self.allergies = allergies
        self.complaint = complaint
        self.occupation = occupation
        self.medication = medication
        super().__init__()
        
    def __repr__(self):
        return "<{} {} {}>".format(self.allergies, self.complaint)
