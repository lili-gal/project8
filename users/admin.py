from django.contrib import admin
from users.models import User, Course, Lesson

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lesson)
