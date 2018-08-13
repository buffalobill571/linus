from django.db import models


class EmailMessage(models.Model):
    email = models.CharField(max_length=50)
    body = models.TextField()
