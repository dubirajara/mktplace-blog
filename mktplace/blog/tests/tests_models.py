from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase, Client

from mktplace.blog.models import Post


class DetailsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'diego'
        self.email = 'test@djangoapp.com'
        self.password = 'test'
        user = User.objects.create_user(
            self.username, self.email, self.password
        )

        self.blog = Post.objects.create(
            user=user, title='test app', tags='django'
        )

    def test_create(self):
        """Check models data create"""
        self.assertTrue(Post.objects.exists())

    def test_str(self):
        """Check __str__ return title field"""
        self.assertEqual('test app', str(self.blog))
