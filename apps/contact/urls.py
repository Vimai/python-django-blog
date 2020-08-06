from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('review', views.review, name='review-contact'),
]
