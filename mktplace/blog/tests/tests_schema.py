import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from mktplace.blog.models import Post
from mktplace.blog.schema import schema


class SchemaTestCase(TestCase):
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

    def test_all_posts(self):
        """GET all posts graphql schema"""
        query = '''
        query{
          allPosts{
            user {
                id
                username
                email
                }
            id
            title
            }
        }
        '''
        result = schema.execute(query)
        assert not result.errors
        expected = {
            "allPosts": [
                {
                    "user": {
                        "id": str(self.blog.id),
                        "username": self.username,
                        "email": self.email,
                    },
                    "id": str(self.blog.id),
                    "title": self.blog.title
                }
            ]
        }

        prettified_data = json.dumps(result.data, sort_keys=False)
        self.assertEqual(json.loads(prettified_data), expected)

    def test_all_users(self):
        """GET all users graphql schema"""
        query = '''
        query{
          allUsers{
            id
            username
            email
        }
        }
        '''
        result = schema.execute(query)
        assert not result.errors
        expected = {
            "allUsers": [
                {
                    "id": str(self.blog.id),
                    "username": self.username,
                    "email": self.email,

                }
            ]
        }

        prettified_data = json.dumps(result.data, sort_keys=False)
        self.assertEqual(json.loads(prettified_data), expected)

    def test_resolve_post_id(self):
        """GET id posts graphql schema"""
        query = (f'''
        query{{
          post(id:{self.blog.id}){{
              user {{
                    id
                    username
                    email
                    }}
                id
                title
            }}
        }}
        ''')
        result = schema.execute(query)
        assert not result.errors
        expected = {
            "post":
                {
                 "user": {
                     "id": str(self.blog.id),
                     "username": self.username,
                     "email": self.email,
                 },
                 "id": str(self.blog.id),
                 "title": self.blog.title
                }
            }

        prettified_data = json.dumps(result.data, sort_keys=False)
        self.assertEqual(json.loads(prettified_data), expected)

    def test_resolve_post_title(self):
        """GET title posts graphql schema"""
        query = '''
        query{
          post(title:"test app"){
              user {
                    id
                    username
                    email
                    }
                id
                title
            }
        }
        '''
        result = schema.execute(query)
        assert not result.errors
        expected = {
            "post":
                {
                 "user": {
                     "id": str(self.blog.id),
                     "username": self.username,
                     "email": self.email,
                 },
                 "id": str(self.blog.id),
                 "title": self.blog.title
                }
            }

        prettified_data = json.dumps(result.data, sort_keys=False)
        self.assertEqual(json.loads(prettified_data), expected)

    def test_resolve_user_id(self):
        query = (f'''
        query{{
          user(id:{self.blog.id}){{
                    id
                    username
                    email
                    }}
            }}
        ''')

        result = schema.execute(query)
        assert not result.errors
        expected = {
            "user": {
               "id": str(self.blog.id),
               "username": self.username,
               "email": self.email,

            }}

        prettified_data = json.dumps(result.data, sort_keys=False)
        self.assertEqual(json.loads(prettified_data), expected)

    def test_resolve_user_username(self):
        query = '''
        query{
          user(username:"diego"){
                    id
                    username
                    email
                    }
            }
        '''
        result = schema.execute(query)
        assert not result.errors
        expected = {
            "user": {
               "id": str(self.blog.id),
               "username": self.username,
               "email": self.email,

            }}

        prettified_data = json.dumps(result.data, sort_keys=False)
        self.assertEqual(json.loads(prettified_data), expected)
