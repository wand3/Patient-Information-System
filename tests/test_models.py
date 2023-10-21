#!/usr/bin/env python3
import unittest
from datetime import datetime
from webapp import create_app, db
from models.base_model import Patient, History
import models

Patients = models.models.P
class PatientModelTestCase(unittest.TestCase):
    """
    Patient model testcase
    """

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  Patient Class  .........')
        print('.................................\n\n')
        
    def setUp(self) -> None:
        """initializes new city for testing"""
        self.city = City()
        self.app = create_app('TestConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()