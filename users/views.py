from django.shortcuts import render, get_object_or_404

# from .models import Users


def signup(request, post_id):
    pass


def login(request, post_id):
    # post_object = get_object_or_404(Post, pk=post_id)
    # data = {
    #     'post': post_object
    # }
    return render(request, 'post.html')


def logout(request, post_id):
    # post_object = get_object_or_404(Post, pk=post_id)
    # data = {
    #     'post': post_object
    # }
    return render(request, 'post.html')


def dashboard(request, post_id):
    # post_object = get_object_or_404(Post, pk=post_id)
    # data = {
    #     'post': post_object
    # }
    return render(request, 'post.html')