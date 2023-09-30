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
