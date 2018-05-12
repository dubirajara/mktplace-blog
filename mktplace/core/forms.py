from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'name': 'name',
                'class': 'form-control name-field',
                'required': 'required',
                'placeholder': 'Nombre',

            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'name': 'email',
                'class': 'form-control mail-field',
                'required': 'required',
                'placeholder': 'Correo',
                }
            )
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                'name': 'message',
                'id': 'message',
                'class': 'form-control',
                'required': 'required',
                'rows': '8',
                'placeholder': 'Mensaje',
            }
        )
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')

        context = {
            'name': name,
            'email': email,
            'message': message
        }

        msg_plain = render_to_string('email.txt', context)

        if not context:
            raise forms.ValidationError('You have to write something!')
        else:
            send_mail(
                'Formulario Contacto Marketing',
                msg_plain,
                email,
                [settings.DEFAULT_FROM_EMAIL]
            )
