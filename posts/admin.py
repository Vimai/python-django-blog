from django.contrib import admin

# Register your models here.
from posts.models import Post

class ListPosts(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('category', )
    list_per_page = 25


admin.site.register(Post, ListPosts)
# django-ckeditor
# Pillow