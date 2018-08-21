from django.db import models


class EmailMessage(models.Model):
    email = models.EmailField(max_length=50)
    body = models.TextField()
    phone = models.CharField(max_length=50, null=True, blank=True)


class AdminEmail(models.Model):
    email = models.EmailField()
