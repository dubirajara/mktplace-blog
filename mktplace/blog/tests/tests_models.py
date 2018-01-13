from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
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

    def test_get_absolute_url(self):
        """Check get_absolute_url slug blog_details url"""
        url = r('post_details', slug=self.blog.slug)
        self.assertEqual(url, self.blog.get_absolute_url())

    def test_tags_can_be_blank(self):
        """Check tags field can be blank"""
        field = Post._meta.get_field('tags')
        self.assertTrue(field.blank)

    def test_content_can_be_blank(self):
        """Check content field can be blank"""
        field = Post._meta.get_field('content')
        self.assertTrue(field.blank)

    def test_photo_can_be_null(self):
        """Check photo field can be null"""
        field = Post._meta.get_field('photo')
        self.assertTrue(field.null)

    def test_slug_null(self):
        """Check slug field cant be null"""
        field = Post._meta.get_field('slug')
        self.assertFalse(field.null)

    def test_ordering(self):
        """Check ordering to show"""
        self.assertListEqual(['-created_at'], Post._meta.ordering)

    def test_create_at(self):
        """Ideas must have an auto created_at attr."""
        self.assertIsInstance(self.blog.created_at, datetime)
