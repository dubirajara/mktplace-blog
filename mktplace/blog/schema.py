import graphene
from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType

from .models import Post


class UserType(DjangoObjectType):
    class Meta:
        model = User
        only_fields = ('username', 'email', 'id')


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    all_users = graphene.List(UserType)

    user = graphene.Field(UserType,
                          id=graphene.Int(),
                          username=graphene.String())

    post = graphene.Field(PostType,
                          id=graphene.Int(),
                          title=graphene.String())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Post.objects.get(pk=id)

        if title is not None:
            return Post.objects.get(title=title)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
            return User.objects.get(pk=id)

        if username is not None:
            return User.objects.get(username=username)


schema = graphene.Schema(query=Query)
