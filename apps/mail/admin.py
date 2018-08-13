from django.contrib import admin

from apps.mail.models import EmailMessage


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    pass
