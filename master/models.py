from django.db import models
from service.models import Service


# Create your models here.
class Master(models.Model):
    RANG_CHOICES = (
        (0, 'Ранг 1'),
        (1, 'Ранг 2')
    )
    name = models.CharField(max_length=255, verbose_name='Имя мастера')
    rang = models.IntegerField(default=0, choices=RANG_CHOICES, verbose_name='Ранг')
    phone = models.IntegerField(verbose_name='Телефон')
    service = models.ManyToManyField(Service, verbose_name='Услуги')
    status = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'masters'
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'
