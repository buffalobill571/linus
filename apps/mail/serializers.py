from rest_framework import serializers

from apps.mail.models import EmailMessage
from apps.mail.tasks import send_notification


class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailMessage
        fields = '__all__'

    def create(self, validated_data):
        obj = super(EmailMessageSerializer, self).create(validated_data)
        send_notification.delay(obj.pk)
        return obj
