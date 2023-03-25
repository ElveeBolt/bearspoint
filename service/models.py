from django.db import models


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание услуги')
    time = models.IntegerField(verbose_name='Продолжительность (в мин.)')
    price = models.IntegerField(verbose_name='Стоимость услуги')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'services'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

