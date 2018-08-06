from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True, related_query_name='posts')
    body = models.TextField()
    image = models.FileField(upload_to='blog/posts/')
    published_date = models.DateTimeField(auto_now_add=True)


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
