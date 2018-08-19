from django.contrib import messages
from django.conf import settings
from django.views.generic import FormView

from mktplace.blog.models import Post
from mktplace.core.forms import ContactForm


class FormListMixin(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(FormListMixin, self).get_context_data(**kwargs)
        context['META_DESCRIPTION'] = settings.META_DESCRIPTION
        context['META_TITLE'] = settings.META_TITLE
        context['posts'] = Post.objects.all()[0:3]

        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            'Correo enviado correctamente! Gracias por contactar con nosotros. En breve te contestaremos.')
        return super().form_valid(form)
