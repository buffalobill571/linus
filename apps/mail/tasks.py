from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail
from django.template import loader

from apps.mail.models import EmailMessage as CustomEmail


@shared_task
def send_notification(mes_id):
    mes = CustomEmail.objects.get(pk=mes_id)

    address = mes.email
    body = mes.body

    subject = 'Notification'
    email_tmp = loader.render_to_string(
        'mail/notification.html',
        {
            'email': address,
            'body': body
        }
    )

    from_mail = settings.EMAIL_HOST_USER
    to_list = [settings.ADMIN_EMAIL]
    send_mail(subject, 'Capital', from_mail, to_list,
              fail_silently=False, html_message=email_tmp)
    mes.delete()
