from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


def index(request):
    posts = Post.objects.order_by('-created_at').filter(published=True)
    paginator = Paginator(posts, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    data = {
        'posts': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'blog.html', data)


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