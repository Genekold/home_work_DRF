from celery import shared_task

from config import settings
from django.core.mail import send_mail

from lms.models import Course
from users.models import User


@shared_task
def send_message_when_update_course(course_id, course_name):
    """Отправка сообщения подписчикам курса об обновлении курса."""

    users = User.objects.filter(subscription__course_id=course_id)
    email_list = []
    for user in users:
        email_list.append(user.email)

    send_mail(f'Обновление курса {course_id}!', f'Курс \"{course_name}\" из ваших подписок обновлен',
              settings.EMAIL_HOST_USER, recipient_list=email_list)
