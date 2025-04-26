from django.contrib import admin

from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
    exclude = ('password',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'payment_date',
        'paid_course_lesson',
        'payment_amount',
        'payment_method',
    )

