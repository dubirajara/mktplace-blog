import json
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from mktplace.blog.schema import schema

from mktplace.blog.models import Post


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

    def test_correct_fetch(self):
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
                        "id": "1",
                        "username": self.username,
                        "email": self.email,
                    },
                    "id": "1",
                    "title": self.blog.title
                }
            ]
        }

        prettified_data = json.dumps(result.data, sort_keys=False)
        self.assertEqual(json.loads(prettified_data), expected)

