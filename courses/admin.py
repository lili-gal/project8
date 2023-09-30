from django.contrib import admin
from courses.models import Course, Lesson, Payment

admin.site.register(Course)
admin.site.register(Lesson)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'course', 'sum')