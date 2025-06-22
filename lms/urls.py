from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonDestroyApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView,
    SubscriptionAPIView,
)

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson-retrieve"),
    path("lesson/create/", LessonCreateApiView.as_view(), name="lesson-create"),
    path(
        "lesson/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson-delete"
    ),
    path(
        "lesson/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson-update"
    ),
    path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
] + router.urls
