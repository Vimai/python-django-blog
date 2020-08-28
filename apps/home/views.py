from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def blog_index(request):
    return render(request, 'home.html')
