from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=100, verbose_name='Город')
    avatar = models.ImageField(upload_to='uploads/', verbose_name='Аватар', **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='uploads/', verbose_name='Аватар', **NULLABLE)
    description = models.TextField(max_length=1000, verbose_name='Описание')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='uploads/', verbose_name='Аватар', **NULLABLE)
    description = models.TextField(max_length=1000, verbose_name='Описание')
    link = models.TextField(verbose_name='Ссылка')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
