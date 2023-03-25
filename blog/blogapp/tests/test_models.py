from django.test import TestCase
from django.urls import reverse
from authentication.models import User
from blogapp.models import Blog
from utils.test_setup import TestSetup

class TestModels(TestSetup):

    def test_should_create_blog(self):
        user = self.create_test_user()
        blog = Blog(owner = user, title="nexus", body = "why nexus")
        blog.save()
        self.assertEqual(str(blog), 'nexus')