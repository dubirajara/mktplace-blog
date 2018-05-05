from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from mktplace.blog.mixins import TagsListMixin
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

    def get_object(self, **kwargs):
        """Returns the BlogPost instance that the view displays"""
        return get_object_or_404(Post, slug=self.kwargs.get("slug"))


tags_list = TagsListMixin.as_view()
