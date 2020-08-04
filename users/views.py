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


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if not email.strip():
            return redirect('login')
        if not password.strip():
            return redirect('login')

        if User.objects.filter(email=email).exists():
            user_name = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=user_name, password=password)
            if user:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                return redirect('login')

    return render(request, 'users/login.html')


def logout(request, post_id):

    return render(request, 'post.html')


def dashboard(request):
    print('ddashboard')
    return render(request, 'users/dashboard.html')
