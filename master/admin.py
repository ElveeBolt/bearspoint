from django.contrib import admin
from .models import Master, Calendar


# Register your models here.
@admin.register(Master)
class Master(admin.ModelAdmin):
    list_display = ('name', 'rang', 'phone', 'status')
    list_filter = ('name', 'rang', 'phone', 'status')


@admin.register(Calendar)
class Calendar(admin.ModelAdmin):
    list_display = ('master', 'date', 'time_start', 'time_end')
    list_filter = ('master', 'date')
