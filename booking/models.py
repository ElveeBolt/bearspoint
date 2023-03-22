from django.contrib.auth.models import User
from django.db import models
from master.models import Master
from service.models import Service


# Create your models here.
class Booking(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    time_start = models.TimeField(verbose_name='Время начала')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.master

    class Meta:
        db_table = 'bookings'
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
