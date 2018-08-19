from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic.base import View

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
