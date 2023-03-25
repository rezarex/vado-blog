from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages

class TestViews(TestCase):

    def test_should_show_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")

    def test_should_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")

    def test_should_signup_user(self):
        self.user = {
            "username":"username",
            "email":"email@gmail.com",
            "password":"password",
            "password2":"password",

        }
        

        response = self.client.post(reverse("register"), self.user)
        self.assertEquals(response.status_code, 302)

    
    def test_should_not_signup_user_with_username_taken(self):
        self.user = {
            "username":"username",
            "email":"email@gmail.com",
            "password":"password",
            "password2":"password",

        }

        self.client.post(reverse("register"), self.user)
        response = self.client.post(reverse("register"), self.user)
        self.assertEquals(response.status_code, 409)


        storage = get_messages(response.wsgi_request)

        error = []

        #loop through and append each message in errors message
        

        self.assertIn("Username taken, please choose another one", list(map(lambda x: x.message, storage)))

        #import python debugger
        # import pdb
        # pdb.set_trace()


    def test_should_not_signup_user_with_email_taken(self):
        self.user = {
            "username":"username",
            "email":"email@gmail.com",
            "password":"password",
            "password2":"password",

        }

        self.user_2 = {
            "username":"username1",
            "email":"email@gmail.com",
            "password":"password",
            "password2":"password",

        }

        self.client.post(reverse("register"), self.user)
        response = self.client.post(reverse("register"), self.user_2)
        self.assertEquals(response.status_code, 409)