from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    data = {
        1: 'ola',
        2: 'mundo'
    }
    dados = {
        'data': data
    }
    return render(request, 'index.html', dados)


def post(request):
    return render(request, 'post.html')
