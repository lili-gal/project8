from django.db import models

from courses.permissions import IsOwnerOrStaff
from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    users = models.ManyToManyField(User, null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='uploads/', verbose_name='Аватар', **NULLABLE)
    description = models.TextField(max_length=1000, verbose_name='Описание')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    users = models.ManyToManyField(User, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name="Курс")
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='uploads/', verbose_name='Аватар', **NULLABLE)
    description = models.TextField(max_length=1000, verbose_name='Описание')
    link = models.TextField(verbose_name='Ссылка')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    payment_date = models.DateField(auto_now_add=True, verbose_name="Дата платежа")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс")
    sum = models.IntegerField(verbose_name="Сумма оплаты")

    class PayMethod(models.TextChoices):
        CASH = 'Наличные',
        TRANSFER = 'Перевод на счёт'

    paymethod = models.CharField(max_length=15, choices=PayMethod.choices, default=PayMethod.TRANSFER, verbose_name="Способ оплаты")