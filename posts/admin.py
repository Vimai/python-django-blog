from django.contrib import admin

# Register your models here.
from posts.models import Post, PostCategory


class ListPosts(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'published')
    list_display_links = ('id', 'title')
    list_editable = ('published', )
    search_fields = ('title', )
    list_filter = ('category', )
    list_per_page = 25


admin.site.register(Post, ListPosts)
admin.site.register(PostCategory)
# django-ckeditor
# Pillow