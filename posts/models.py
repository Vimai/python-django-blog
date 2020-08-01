from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=10000)
    updated_date = models.DateTimeField('date published')
    created_date = models.DateTimeField('date published')