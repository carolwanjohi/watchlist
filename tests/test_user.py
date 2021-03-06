import unittest
from app.models import User

class UserTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password='banana')

    def test_password_setter(self):
        '''
        Test case to ascertain when a password is being hashed and pass_secure contains a value
        '''
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        '''
        Test case to confirm the application raises an AttributeError when we try to access the password property
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        Test case that confirms that our user password_hash can be verified when we pass in the correct the password
        '''
        self.assertTrue(self.new_user.verify_password('banana'))



