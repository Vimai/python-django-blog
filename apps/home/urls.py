from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog_index, name='blog_index'),
]