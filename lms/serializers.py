from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализатор курса"""
    lessons = SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons(self, obj):
        return [lesson.name for lesson in obj.lessons.all()]


class LessonDetailSerializer(ModelSerializer):
    """Сериализатор детальног представления урока"""
    lessons_in_the_course = SerializerMethodField()
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = ('name', 'preview', 'description', 'lessons_in_the_course', 'course' )

    def get_lessons_in_the_course(self, obj):
        return Lesson.objects.filter(course=obj.course).count()


class LessonSerializer(ModelSerializer):
    """Сериализатор урока"""
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = "__all__"
