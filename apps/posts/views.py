from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


def index(request):
    posts = Post.objects.order_by('-created_at').filter(published=True)
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_per_page = paginator.get_page(page)
    data = {
        'posts': posts_per_page
    }
    return render(request, 'index.html', data)


def post(request, post_id):
    post_object = get_object_or_404(Post, pk=post_id)
    data = {
        'post': post_object
    }
    return render(request, 'post.html', data)


def search(request):
    posts = Post.objects.order_by('-created_at').filter(published=True)
    if 'search' in request.GET:
        possible_titles = request.GET['search']
        if possible_titles:
            posts = posts.filter(title__icontains=possible_titles)

    data = {
        'posts': posts
    }
    return render(request, 'search.html', data)