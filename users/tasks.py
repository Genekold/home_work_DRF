from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.utils import timezone

from users.models import User


@shared_task
def block_user_not_active():
    """Блокирует пользователя, который не заходил 30 дней."""

    month_ago = timezone.now() - relativedelta(months=1)
    users = User.objects.all().exclude(Q(groups__name="moder") | Q(is_superuser=True)).filter(is_active=True,
                                                                                              last_login__lt=month_ago)
    users.update(is_active=False)
