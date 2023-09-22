from rest_framework import serializers

from courses.models import Course, Lesson, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(read_only=True, many=True, source='payment_set.all')
    lessons = LessonSerializer(read_only=True, many=True, source='lesson_set.all')
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson_set.all().count()

    class Meta:
        model = Course
        fields = ['id', 'lesson_count', 'name', 'image', 'description', 'lessons', 'payment']
