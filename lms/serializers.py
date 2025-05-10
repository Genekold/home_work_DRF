from rest_framework import serializers
from lms.models import Course, Lesson, Subscription
from lms.validators import validate_url


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор курса"""

    lessons_in_the_course = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_in_the_course(self, obj):
        return obj.lessons.count()

    def get_subscription(self, obj):
        user = self.context["request"].user
        return Subscription.objects.all().filter(user=user).filter(course=obj).exists()


class LessonDetailSerializer(serializers.ModelSerializer):
    """Сериализатор детальног представления урока"""

    class Meta:
        model = Lesson
        fields = (
            "name",
            "preview",
            "description",
            "course",
            "owner"
        )


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор урока"""

    course = CourseSerializer(read_only=True)

    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course',
        write_only=True,
        required=True
    )
    url = serializers.URLField(validators=[validate_url], required=False)

    class Meta:
        model = Lesson
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки"""

    class Meta:
        model = Subscription
        fields = "__all__"
