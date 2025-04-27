from django.core.management.base import BaseCommand

from lms.models import Course
from users.models import User


class Command(BaseCommand):
    help = 'Добавляет пользователя и оплату за курсы и уроки'

    def handle(self, *args, **options):

        # payments = [
        #     {'user': user, 'paid_course_lesson': 'lesson', 'payment_amount': 1000, 'payment_method': 'trans'},
        #     {'user': user, 'paid_course_lesson': 'course', 'payment_amount': 5000, 'payment_method': 'cash'},
        #     {'user': user, 'paid_course_lesson': 'lesson', 'payment_amount': 500, 'payment_method': 'trans'},
        # ]

        lessons = [
            {'pk': 10, 'name': 'Сложение', },
            {'pk': 11, 'name': 'Умножение'},
            {'pk': 12, 'name': 'История'},
            {'pk': 12, 'name': 'История'},
            {'pk': 12, 'name': 'История'},
            {'pk': 12, 'name': 'История'},
        ]

        user1 = User.objects.create(pk=10, email='user1@mail.ru')
        user1.set_password('Qwe123')
        user1.save()
        user2 = User.objects.create(pk=11, email='user2@mail.ru')
        user2.set_password('Qwe123')
        user2.save()

        course1 = Course.objects.create(pk=10, name='Математика')
        course2 = Course.objects.create(pk=11, name='Русский язык')
        course3 = Course.objects.create(pk=12, name='История')

