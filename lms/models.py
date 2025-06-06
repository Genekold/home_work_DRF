from django.db import models

from config import settings


class Course(models.Model):
    """Модель курса"""

    name = models.CharField(
        max_length=150, verbose_name="Название курса", help_text="Введите назвние курса"
    )
    preview = models.ImageField(
        upload_to="lms/photo/course/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Превью курса",
        help_text="Загрузите фото",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание курса", help_text="Опишите курс"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.name}"


class Lesson(models.Model):
    """Модель урока"""

    name = models.CharField(
        max_length=150, verbose_name="Название урока", help_text="Введите назвние урока"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание урока", help_text="Опишите урок"
    )
    preview = models.ImageField(
        upload_to="lms/photo/lesson/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Превью урока",
        help_text="Загрузите фото",
    )
    url = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Укажите курс",
        related_name="lessons",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.course.name} - {self.name}"


class Subscription(models.Model):
    """Модель подписки на курс"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс в подписке",
        related_name="subscriptions"
    )

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
