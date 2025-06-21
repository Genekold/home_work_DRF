import re
from rest_framework.serializers import ValidationError

pattern = re.compile(r"youtube\.com")


def validate_url(url):
    if not pattern.search(url):
        raise ValidationError(
            "Ссылки на сторонние ресурсы (кроме youtube.com) запрещены"
        )
