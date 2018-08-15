from django.db import models


class EmailMessage(models.Model):
    email = models.EmailField(max_length=50)
    body = models.TextField()


class AdminEmail(models.Model):
    email = models.EmailField()
