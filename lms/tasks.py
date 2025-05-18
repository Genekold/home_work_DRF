from celery import shared_task
from django.db.models import Q
from django.utils import timezone

from config import settings
from django.core.mail import send_mail

from users.models import User


@shared_task
def send_message_when_update_course(course, email_list):
    """Отправка сообщения подписчикам курса об обновлении курса."""

    send_mail(f'Обновление курса {course}!', f'Курс {course} из ваших подписок обновлен', settings.EMAIL_HOST_USER,
              recipient_list=email_list)

@shared_task
def block_user_not_active():
    """Блокирует пользователя, который не заходил 30 дней."""

    today = timezone.now()
    users = User.objects.all().exclude(Q(groups__name="moder") | Q(is_superuser=True))

    for user in users:
        delta = today - user.last_login
        if delta.days >= 30:
            user.is_active = False
            user.save()
