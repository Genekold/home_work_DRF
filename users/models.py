from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватат",
        help_text="Загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Payments(models.Model):

    PAID_CHOISES = [
        ("course", "course"),
        ("lesson", "lesson"),
    ]
    METHOD_CHOISES = [
        ("cash", "cash"),
        ("trans", "trans")
    ]
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    payment_date = models.DateTimeField(verbose_name="Дата оплаты", auto_now_add=True)
    paid_course_lesson = models.CharField(max_length=6, choices=PAID_CHOISES, verbose_name='Оплаченный курс/урок')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Оплаченый курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Оплаченый урок')
    payment_amount = models.PositiveIntegerField(verbose_name='Суммма оплаты')
    payment_method = models.CharField(max_length=5, choices=METHOD_CHOISES, verbose_name="Способ оплаты")

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплата"

    def get_paid_course_lesson(self):
        if self.paid_course_lesson == 'course':
            return self.paid_course
        elif self.paid_course_lesson == 'lesson':
            return self.paid_lesson

