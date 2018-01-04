from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

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
        
    def test_create(self):
        """Check models data create"""
        self.assertTrue(Post.objects.exists())
        
    def test_str(self):
        """Check __str__ return title field"""
        self.assertEqual('test app', str(self.blog))

    def test_get_tags(self):
        """GET 'Ideas tags' must return status code 200"""
        response = self.client.get(r('tag', self.blog.tags))
        self.assertEqual(200, response.status_code)


class BlogTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('post_list'))

    def test_get(self):
        """GET 'blog' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'blog' must use template blog.html and base.html"""
        self.assertTemplateUsed(self.response, 'blog.html')
        self.assertTemplateUsed(self.response, 'baseblog.html')
        self.assertTemplateUsed(self.response, 'footer.html')
