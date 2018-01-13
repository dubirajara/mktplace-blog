import tagulous.admin
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'active', 'created_at')
    list_editable = ('active',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.site_header = 'The Marketing Place Admin'
admin.site.site_title = 'The Marketing Place Admin'
admin.site.register(Post, PostAdmin)
tagulous.admin.register(Post.tags.tag_model)
