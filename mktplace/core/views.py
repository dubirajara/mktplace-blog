from django.conf import settings
from django.views.generic import TemplateView, FormView


from mktplace.blog.models import Post
from .forms import ContactForm


class HomeView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/success/'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['META_DESCRIPTION'] = settings.META_DESCRIPTION
        context['META_TITLE'] = settings.META_TITLE
        context['posts'] = Post.objects.all()[0:3]

        return context

    def form_valid(self, form):
        form.clean()
        return super().form_valid(form)


success = TemplateView.as_view(template_name='success.html')
