from django.test import TestCase
from django.contrib.auth.models import User

from yolo.models import UserProfile


class RegistrationTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('vasek', 'vasek@deneg.net', '12345')

    def test_is_user_profile_created(self):
        """new UserProfile instance should be created every time a new user is created"""
        user = User.objects.get(username='vasek')
        self.assertIsNotNone(user.profile)




