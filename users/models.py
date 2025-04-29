from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

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


class Payment(models.Model):
    PAYMENT_TYPE_CHOISES = [
        ("course", "Курс"),
        ("lesson", "Урок"),
    ]
    PAYMENT_METHOD_CHOISES = [
        ("cash", "Наличные"),
        ("trans", "Перевод")
    ]
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        verbose_name="Пользователь"
    )
    payment_date = models.DateTimeField(
        auto_now_add = True,
        verbose_name="Дата оплаты"
    )
    payment_type = models.CharField(
        max_length=6,
        choices=PAYMENT_TYPE_CHOISES,
        verbose_name='Тип оплаты')
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Курс'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Урок'
    )
    payment_amount = models.PositiveIntegerField(
        verbose_name='Суммма оплаты'
    )
    payment_method = models.CharField(
        max_length=5,
        choices=PAYMENT_METHOD_CHOISES,
        verbose_name="Способ оплаты")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ["-payment_date"]

    def __str__(self):
        return f"Платеж {self.id} - {self.user}"

    def clean(self):
        super().clean()

        if self.payment_type == "course" and not self.course:
            raise ValidationError("Для типа 'курс' необходимо указать курс.")
        elif self.payment_type == "lesson" and not self.lesson:
            raise ValidationError("Для типа 'урок' необходимо указать урок.")

        if self.payment_type == "course" and self.lesson:
            raise ValidationError("Для типа 'курс' не должно быть указано урока.")
        elif self.payment_type == "lesson" and not self.course:
            raise ValidationError("Для типа 'урок' не должно быть указано курса")
