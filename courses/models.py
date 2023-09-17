from django.db import models


NULLABLE = {'blank': True, 'null': True}


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
