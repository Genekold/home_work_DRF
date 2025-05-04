from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from lms.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = "Добавляет пользователя и оплату за курсы и уроки"

    def handle(self, *args, **options):
        moder = User.objects.create(email="moder@mail.ru")
        moder.set_password("qwe123")
        moder.save()
        user1 = User.objects.create(email="user1@mail.ru")
        user1.set_password("qwe123")
        user1.save()
        user2 = User.objects.create(email="user2@mail.ru")
        user2.set_password("qwe123")
        user2.save()

        course1 = Course.objects.create(name="Математика", owner=user1)
        course2 = Course.objects.create(name="Русский язык", owner=user2)
        course3 = Course.objects.create(name="Литература", owner=user1)

        lesson1 = Lesson.objects.create(name="Сложение", course=course1, owner=user1)
        lesson2 = Lesson.objects.create(name="Умножение", course=course1, owner=user1)
        lesson3 = Lesson.objects.create(name="Деление", course=course1, owner=user1)
        lesson4 = Lesson.objects.create(name="Существительные", course=course2, owner=user2)
        lesson5 = Lesson.objects.create(name="Глаголы", course=course2, owner=user2)
        lesson6 = Lesson.objects.create(name="Стихотворения", course=course3, owner=user1)
        lesson7 = Lesson.objects.create(name="Рассказы", course=course3, owner=user1)

        Payment.objects.create(
            user=user1,
            payment_type="lesson",
            lesson=lesson4,
            payment_amount=100,
            payment_method="cash",
        )
        Payment.objects.create(
            user=user2,
            payment_type="course",
            course=course1,
            payment_amount=1000,
            payment_method="cash",
        )
        Payment.objects.create(
            user=user1,
            payment_type="course",
            course=course2,
            payment_amount=2000,
            payment_method="trans",
        )
        Payment.objects.create(
            user=user2,
            payment_type="lesson",
            lesson=lesson6,
            payment_amount=400,
            payment_method="trans",
        )

        moder_group = Group.objects.create(name="moder")
        moder.groups.add(moder_group)

        self.stdout.write(self.style.SUCCESS("Данные загружены!"))
