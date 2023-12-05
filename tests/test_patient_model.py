#!/usr/bin/env python3
import unittest
from datetime import datetime
from config import db_session, TestConfig
from models.patient import Patient
import webapp

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
        self.app = webapp.create_app('TestConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db_session.create_all()

    def tearDown(self) -> None:
        db_session.remove()
        db_session.drop_all()
        self.app_context.pop()


if __name__ == "__main__":
    unittest.main()