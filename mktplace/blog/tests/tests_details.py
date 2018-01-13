from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.test.client import Client

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
        self.response = self.client.get(r(self.blog.get_absolute_url()))

    def test_get(self):
        """GET 'Ideas Details' must return status code 200"""
        self.assertEqual(200, self.response.status_code)
        self.assertTrue('posts' in self.response.context)

    def test_get_tags(self):
        """GET 'Ideas tags' must return status code 200"""
        response = self.client.get(r('tag', self.blog.tags))
        self.assertEqual(200, response.status_code)
        self.assertTrue('tags' in response.context)
