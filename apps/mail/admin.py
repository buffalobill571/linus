from django.contrib import admin

from apps.mail.models import EmailMessage, AdminEmail


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'body')


@admin.register(AdminEmail)
class AdminEmailAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email')
