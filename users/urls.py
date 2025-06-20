from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    PaymentListAPIView,
    UsersCreateAPIView,
    PaymentCreateAPIView,
    MyTokenObtainPairView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment-list"),
    path("register/", UsersCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        MyTokenObtainPairView.as_view(permission_classes=[AllowAny]),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=[AllowAny]),
        name="token-refresh",
    ),
    path("subscription/", PaymentCreateAPIView.as_view(), name="subscription"),
]
