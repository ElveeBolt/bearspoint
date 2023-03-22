from django.contrib import admin
from .models import Service


# Register your models here.
@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ('title', 'time', 'price')