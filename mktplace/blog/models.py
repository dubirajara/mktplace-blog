import tagulous.models
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import resolve_url as r
from django.template.defaultfilters import slugify


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.URLField('Image', null=True)
    title = models.CharField("Titulo", max_length=255)
    content = models.TextField("Contenido", blank=True)
    slug = models.SlugField("Slug", max_length=255)
    tags = tagulous.models.TagField(
        blank=True,
        get_absolute_url=lambda tag: r(
            'blog.views.by_tags', kwargs={'tags': tag.slug}
        ),
        max_count=5,
        force_lowercase=True,
    )
    active = models.BooleanField("Activo", default=True)
    created_at = models.DateTimeField("Creado el", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado el", auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.get_unique_slug()
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return r('post_details', slug=self.slug)
