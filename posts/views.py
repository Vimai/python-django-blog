from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Post


def index(request):
    posts = Post.objects.filter(published=True)
    data = {
        'posts': posts
    }
    return render(request, 'index.html', data)


def post(request, post_id):
    post_object = get_object_or_404(Post, pk=post_id)
    data = {
        'post': post_object
    }
    return render(request, 'post.html', data)
