#!/usr/bin/env python3
from flask import current_app
import unittest
from webapp import create_app
from config import TestConfig, db_session, engine
from models.base_model import Base 


class BasicTestCase(unittest.TestCase):
    """
    test flask application context with appropriate configuration
    in config file (TestConfig)
    """
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        db_session.remove()
        Base.metadata.drop_all(bind=engine)
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # def test_app_is_testing(self):
    #     self.assertTrue(current_app('TestConfig'))


if __name__ == '__main__':
       unittest.main()