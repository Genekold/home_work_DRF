from rest_framework import serializers
from lms.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор курса"""

    lessons_in_the_course = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_in_the_course(self, obj):
        return obj.lessons.count()


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

    class Meta:
        model = Lesson
        fields = "__all__"
