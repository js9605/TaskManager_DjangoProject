from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserRegistrationTest(TestCase):
    def test_user_registration_view(self):
        url = reverse("register")
        response = self.client.get(url)

        self.assertTemplateUsed(response, "register.html")
        self.assertEqual(response.status_code, 200)

        user_data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "testpassword",
        }

        response = self.client.post(url, data=user_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")
