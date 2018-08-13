from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny

from apps.mail.serializers import EmailMessageSerializer


class SendMailView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailMessageSerializer
