from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Добавляет пользователя и оплату за курсы и уроки'

    def handle(self, *args, **options):
        user = User.objects.create(email="example@mail.ru")
        user.set_password('Qwe123')
        user.save()

        payments = [
            {'user': user, 'paid_course_lesson': 'lesson', 'payment_amount': 1000, 'payment_method': 'trans'},
            {'user': user, 'paid_course_lesson': 'course', 'payment_amount': 5000, 'payment_method': 'cash'},
            {'user': user, 'paid_course_lesson': 'lesson', 'payment_amount': 500, 'payment_method': 'trans'},
        ]


