from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.core import mail
from django.test import TestCase, Client

from mktplace.blog.models import Post
from .forms import ContactForm


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

    def test_html(self):
        """Test contents html"""
        contents = (self.blog.title, self.blog.photo, self.blog.content)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)


class ContactFormTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_has_form_on_context(self):
        self.assertIsInstance(self.response.context['form'], ContactForm)

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = ContactForm()
        expected = ['name', 'email', 'message']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_form_html(self):
        contents = [
            'form-control name-field',
            'required',
            'placeholder',
            'name',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_forms_valid(self):
        form_data = {'name': 'Diego',
                     'email': 'diego@mail.com',
                     'message': 'test form django'
                     }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_forms_invalid(self):
        form_data = {'name': '',
                     'email': '',
                     'message': ''
                     }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_email_error(self):
        form_data = {'name': 'Diego',
                     'email': 'diegomail.com',
                     'message': 'test form django'
                     }
        response = self.client.post(r('home'), form_data)
        self.assertFormError(response, 'form', 'email', 'Introduzca una dirección de correo electrónico válida.')

    def test_forms_blank_error(self):
        form_data = {'name': '',
                     'email': '',
                     'message': ''
                     }
        response = self.client.post(r('home'), form_data)
        self.assertFormError(response, 'form', 'name', 'Este campo es obligatorio.')


class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
