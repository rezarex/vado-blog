from django.test import TestCase
from authentication.models import User
from utils.test_setup import TestSetup

class TestModels(TestSetup):
    
    def test_should_create_user(self):
        user = self.create_test_user()

        self.assertEqual(str(user),user.email )