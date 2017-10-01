from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=75)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

    def send_email(self):
        send_mail(self.subject, self.message, self.sender, 'test@gmail.com', fail_silently=False)
        print('sent')