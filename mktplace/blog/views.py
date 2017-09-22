from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostList(ListView):
    model = Post
    paginate_by = '2'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'blog.html'


class PostDetails(DetailView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'post.html'
