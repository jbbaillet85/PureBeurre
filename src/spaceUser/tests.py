from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import User

# Create your tests here.
class TestCreateUser(TestCase):
    def testCreateUser(self):
        user = User(last_name='jb',email='user@mail.com', password='password')
        self.assertEqual(user.last_name, 'jb')
        self.assertEqual(user.email, 'user@mail.com')
        self.assertEqual(user.password, 'password')