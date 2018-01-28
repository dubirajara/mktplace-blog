from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase, Client

from mktplace.blog.models import Post


class HomeTest(TestCase):
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
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET 'home' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'home' must use template index.html and base.html"""
        self.assertTemplateUsed(self.response, 'index.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_home_links(self):
        """check href link in home"""
        contents = (
            'href="{}"'.format(r('post_list')),
            'href="{}"'.format(r('post_details', self.blog.slug)),
            'href="{}"'.format('mailto:info@themarketingplace.es'),
            'href="{}"'.format('https://www.facebook.com/themarketingplace/'),
            'href="{}"'.format('https://twitter.com/TMarketingPlace'),
            'href="{}"'.format('https://www.linkedin.com/company/the-marketing-place/'),
            'href="{}"'.format('http://themarketingplace.es/'),
        )
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')