from django.core.management.base import BaseCommand

from lms.models import Course, Lesson
from users.models import User, Payment


class Command(BaseCommand):
    help = 'Добавляет пользователя и оплату за курсы и уроки'

    def handle(self, *args, **options):

        user1 = User.objects.create(email='user1@mail.ru')
        user2 = User.objects.create(email='user2@mail.ru')

        course1 = Course.objects.create(name='Математика')
        course2 = Course.objects.create(name='Русский язык')
        course3 = Course.objects.create(name='Литература')

        lesson1 = Lesson.objects.create(name='Сложение', course=course1)
        lesson2 = Lesson.objects.create(name='Умножение', course=course1)
        lesson3 = Lesson.objects.create(name='Деление', course=course1)
        lesson4 = Lesson.objects.create(name='Существительные', course=course2)
        lesson5 = Lesson.objects.create(name='Глаголы', course=course2)
        lesson6 = Lesson.objects.create(name='Стихотворения', course=course3)
        lesson7 = Lesson.objects.create(name='Рассказы', course=course3)

        Payment.objects.create(user=user1, payment_type="lesson", lesson=lesson4, payment_amount=100, payment_method='cash')
        Payment.objects.create(user=user2, payment_type="course", course=course1, payment_amount=1000, payment_method='cash')
        Payment.objects.create(user=user1, payment_type="course", course=course2, payment_amount=2000, payment_method='trans')
        Payment.objects.create(user=user2, payment_type="lesson", lesson=lesson6, payment_amount=400, payment_method='trans')

        self.stdout.write(self.style.SUCCESS('Данные загружены!'))
