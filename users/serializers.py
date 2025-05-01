from rest_framework import serializers

from lms.serializers import CourseSerializer, LessonSerializer
from users.models import Payment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор платежа"""
    course = CourseSerializer()
    lesson = LessonSerializer()
    class Meta:
        model = Payment
        fields = '__all__'
