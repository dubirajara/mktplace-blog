from django.views.generic import ListView, TemplateView
from django.conf import settings

from mktplace.blog.models import Post


class HomeView(ListView):
    paginate_by = '3'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['META_DESCRIPTION'] = settings.META_DESCRIPTION
        context['META_TITLE'] = settings.META_TITLE

        return context


success = TemplateView.as_view(template_name='success.html')
