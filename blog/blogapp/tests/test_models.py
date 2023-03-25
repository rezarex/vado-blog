from django.test import TestCase
from authentication.models import User
from blogapp.models import Blog

class TestModels(TestCase):
    
    def test_should_create_blog(self):
        user = User.objects.create_user(username="username3", email = 'email@app.com')
        user.set_password('password12!')
        user.save()

        blog = Blog(owner = user, title="nexus", body = "why nexus")

        blog.save()
        self.assertEqual(str(blog), 'nexus')