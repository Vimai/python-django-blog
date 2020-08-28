from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('old-home', views.blog_index, name='old_home'),
]