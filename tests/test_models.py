#!/usr/bin/env python3
import unittest
from datetime import datetime
from webapp import create_app, db
from models.models import Patient, History


class PatientModelTestCase(unittest.TestCase):
    """
    Patient model testcase
    """
    def setUp(self) -> None:
        self.app = create_app('TestConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()