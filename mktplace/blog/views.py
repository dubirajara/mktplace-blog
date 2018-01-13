from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from .models import Post


class PostList(ListView):
    model = Post
    paginate_by = '9'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'blog.html'


class PostDetails(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post.html'

    def get_object(self):
        """Returns the BlogPost instance that the view displays"""
        return get_object_or_404(Post, slug=self.kwargs.get("slug"))


def by_tags(request, tags):
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
