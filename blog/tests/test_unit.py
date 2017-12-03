from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import *
from django.utils import timezone

# Create your tests here.
class User(TestCase):
        
    def test_user_exist(self):
        try:
            userdetails = User.objects.filter(username = 'admin')
        except:
            userdetails = None

        if userdetails:
            is_exist = True
        else:
            is_exist = False

        self.assertFalse(is_exist)
