#!/usr/bin/python3
import unittest
from models.user import User
from config import db_session, TestConfig, engine
from webapp import create_app
from models.base_model import Base

# import webapp


class UserModelTestCase(unittest.TestCase):
    """
    User model testcase
    """
    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  User Class  .........')
        print('.................................\n\n')
        
    def setUp(self) -> None:
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        # Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

    # def test_password_setter(self):
    #     u = User(password='one')
    #     self.assertTrue(u.password_hash is not None)

    # def test_verify_password_hash(self):
    #     u = User(password='one')
    #     self.assertTrue(u.verify_password('one'))
    #     self.assertFalse(u.verify_password('yne'))

    # def test_password_salts_are_random(self):
    #     u = User(password='bat')
    #     u2 = User(password='bat')
    #     self.assertTrue(u.password_hash != u2.password_hash)

    




if __name__ == '__main__':
    unittest.main()
