from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализатор курса"""
    lessons = SerializerMethodField()
    lessons_in_the_course = SerializerMethodField()
    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons(self, obj):
        return [lesson.name for lesson in obj.lessons.all()]

    def get_lessons_in_the_course(self, obj):
        return obj.lessons.count()


class LessonDetailSerializer(ModelSerializer):
    """Сериализатор детальног представления урока"""

    class Meta:
        model = Lesson
        fields = ('name', 'preview', 'description', 'course',)


class LessonSerializer(ModelSerializer):
    """Сериализатор урока"""
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = "__all__"

