from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Post


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'active')
    list_editable = ('active',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.site_header = 'MKT Place Admin'
admin.site.register(Post, PostAdmin)
