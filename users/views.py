from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth

# from .models import Users


def signup(request):
    if request.method == 'POST':
        print('user')
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        if not email.strip():
            return redirect('signup')
        if not password.strip():
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            return redirect('signup')

        user = User.objects.create_user(email=email, password=password)
        user.save()

        return redirect('login')
    else:
        print('get')

    return render(request, 'users/signup.html')


def login(request, post_id):
    # post_object = get_object_or_404(Post, pk=post_id)
    # data = {
    #     'post': post_object
    # }
    return render(request, 'post.html')


def logout(request, post_id):

    return render(request, 'post.html')


def dashboard(request):
    print('ddashboard')
    return render(request, 'users/dashboard.html')
