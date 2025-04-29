from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
    exclude = ('password',)


@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'payment_date',
        'payment_type',
        'payment_amount',
        'payment_method',
    )

