from django.test import TestCase
from django.urls import reverse
from authentication.models import User
from blogapp.models import Blog
from utils.test_setup import TestSetup

class TestViews(TestSetup):

    def test_should_create_a_blog(self):

        user = self.create_test_user()
        self.client.post(reverse('login'), {
            'username':user.username,
            'password':'password12'
        })
        blogs = Blog.objects.all()

        self.assertEqual(blogs.count(), 0)

        response = self.client.post(reverse('new-blog'),{
            'owner':user,
            'title':'hello nerds!',
            'body':'first testament!'
        })


        print(response)

        new_blogs = Blog.objects.all()
        self.assertEqual(new_blogs.count(), 0)

        self.assertEqual(response.status_code, 302)
    
    