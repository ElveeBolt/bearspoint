from django.db import models
from service.models import Service
from django.urls import reverse


# Create your models here.
class Master(models.Model):
    RANG_CHOICES = (
        (0, 'Ранг 1'),
        (1, 'Ранг 2')
    )
    STATUS_CHOICES = (
        (0, 'Не активен'),
        (1, 'Активен')
    )
    name = models.CharField(max_length=255, verbose_name='Имя мастера')
    rang = models.IntegerField(default=0, choices=RANG_CHOICES, verbose_name='Ранг')
    phone = models.IntegerField(verbose_name='Телефон')
    service = models.ManyToManyField(Service, verbose_name='Услуги')
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manager_masters')

    class Meta:
        db_table = 'masters'
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Calendar(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')
    date = models.DateField(verbose_name='Дата')
    time_start = models.TimeField(verbose_name='Начало рабочего дня')
    time_end = models.TimeField(verbose_name='Конец рабочего дня')

    def __str__(self):
        return self.master.name

    class Meta:
        db_table = 'calendars'
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'
