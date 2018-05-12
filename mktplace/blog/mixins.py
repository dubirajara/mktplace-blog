from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import View

from mktplace.core.forms import ContactForm
from .models import Post


class TagsListMixin(View):
    def get(self, request, tags):
        queryset = Post.objects.filter(tags=tags)

        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 9)

        try:
            tags = paginator.page(page)
        except PageNotAnInteger:
            tags = paginator.page(1)
        except EmptyPage:
            tags = paginator.page(paginator.num_pages)

        context = {
            'tags': tags,
        }

        return render(request, 'tags.html', context)


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
