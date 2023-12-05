#!/usr/bin/env python3
"""
    Unit Test for BaseModel Class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Class for testing BaseModel class and its methods
    """

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Functions .....')
        print('.....  For BaseModel Class  .....')
        print('.................................\n\n')

    def setUp(self) -> None:
        """initializes new BaseModel instance for testing"""
        self.model = BaseModel()

    def test_instantiation(self):
        """checks if BaseModel is properly instantiated"""
        self.assertIsInstance(self.model, BaseModel)


if __name__ == '__main__':
    unittest.main()