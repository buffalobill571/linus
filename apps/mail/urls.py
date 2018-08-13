from django.urls import path

from apps.mail.views import SendMailView

urlpatterns = [
    path('send-mail/', SendMailView.as_view())
]
