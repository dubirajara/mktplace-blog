from django.test import TestCase
from django.shortcuts import resolve_url as r


class BlogTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('post_list'))

    def test_get(self):
        """GET 'blog' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'blog' must use template blog.html and base.html"""
        self.assertTemplateUsed(self.response, 'blog.html')
        self.assertTemplateUsed(self.response, 'base.html')
