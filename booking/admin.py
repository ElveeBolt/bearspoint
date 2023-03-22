from django.contrib import admin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = ('master', 'service', 'user', 'time_start', 'date')
    list_filter = ('master', 'service', 'user', 'date')
