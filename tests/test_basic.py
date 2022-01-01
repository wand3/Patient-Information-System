#!/usr/bin/env python3
import unittest
from flask import current_app
from webapp import db, create_app
# from config import TestConfig


class BasicTestCase(unittest.TestCase):
    """
    test flask application context with appropriate configuration
    in config file (TestConfig)
    """
    def setUp(self):
        self.app = create_app('config.TestConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # def test_app_is_testing(self):
    #     self.assertTrue(current_app('TestConfig'))


if __name__ == '__main__':
       unittest.main()