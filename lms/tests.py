from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    """Тестирование CRUD уроков"""

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(name="Тестовый курс", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="Тестовый урок", course_id=self.course.pk, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson-retrieve", args=[self.lesson.id])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("lms:lesson-create")
        data = {"name": "Тестовый урок 2", "course_id": self.course.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)
        self.assertEqual(response.data["owner"], self.user.pk)

    def test_lesson_update(self):
        url = reverse("lms:lesson-update", args=[self.lesson.id])
        data = {"name": "Новый тестовый урок"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Новый тестовый урок")

    def test_lesson_delete(self):
        url = reverse("lms:lesson-delete", args=[self.lesson.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)

    def test_lesson_list(self):
        url = reverse("lms:lesson-list")
        response = self.client.get(url)
        self.maxDiff = None
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "course": {
                        "id": self.course.pk,
                        "lessons_in_the_course": 1,
                        "subscription": False,
                        "name": self.course.name,
                        "preview": None,
                        "description": None,
                        "owner": self.user.pk,
                    },
                    "url": None,
                    "name": self.lesson.name,
                    "description": None,
                    "preview": None,
                    "owner": self.user.pk,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class CourseTestCase(APITestCase):
    """Тестирование CRUD курсов"""

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(name="Тестовый курс", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="Тестовый урок", course_id=self.course.pk, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_course_detail(self):
        url = reverse("lms:course-detail", args=[self.course.id])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)

    def test_course_create(self):
        url = reverse("lms:course-list")
        data = {"name": "Тестовый курс 2"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)
        self.assertEqual(response.data["owner"], self.user.pk)

    def test_course_update(self):
        url = reverse("lms:course-detail", args=[self.course.id])
        data = {"name": "Новый тестовый курс"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Новый тестовый курс")

    def test_course_delete(self):
        url = reverse("lms:course-detail", args=[self.course.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)

    def test_course_list(self):
        url = reverse("lms:course-list")
        response = self.client.get(url)
        self.maxDiff = None
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "lessons_in_the_course": 1,
                    "subscription": False,
                    "name": self.course.name,
                    "preview": None,
                    "description": None,
                    "owner": self.user.pk,
                },
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    """Тестирование добавления и удаления подписки на курс"""

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(name="Тестовый курс", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        url = reverse("lms:subscription")
        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка добавлена")

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка удалена")
