from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_new_user_with_email_successful(self):
        """Test creating a new user with an email is sucessful"""
        email = "sheery@gmail.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if new email is normalized"""
        email = 'sherry@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email, password="test123"
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a new user without email  raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test124")

    def test_create_new_super_user(self):
        """Test creating a super user"""
        user = get_user_model().objects.create_superuser(
            "sherry@gmail.com",
            "test@123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
