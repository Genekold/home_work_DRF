from rest_framework import serializers

from lms.serializers import CourseSerializer, LessonSerializer
from users.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор платежа"""
    course = CourseSerializer()
    lesson = LessonSerializer()
    class Meta:
        model = Payment
        fields = '__all__'
