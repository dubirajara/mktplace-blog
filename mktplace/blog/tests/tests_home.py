from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from mktplace.blog.models import Post


class BlogTest(TestCase):
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
        self.response = self.client.get(r('post_list'))

    def test_get(self):
        """GET 'blog' must return status code 200"""
        self.assertEqual(200, self.response.status_code)
        self.assertTrue('posts' in self.response.context)

    def test_template(self):
        """'blog' must use template blog.html and base.html"""
        self.assertTemplateUsed(self.response, 'blog.html')
        self.assertTemplateUsed(self.response, 'baseblog.html')
        self.assertTemplateUsed(self.response, 'footer.html')
