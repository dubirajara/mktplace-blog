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


class ThanksContactView(TemplateView):
    template_name = 'success.html'


# def email(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "email.html", {'form': form})
#
#
# def success(request):
#     return HttpResponse('Success! Thank you for your message.')