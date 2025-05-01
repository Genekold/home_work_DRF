from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UsersCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method',)
    ordering_fields = ('payment_date',)
