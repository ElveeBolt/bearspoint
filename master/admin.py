from django.contrib import admin
from .models import Master


# Register your models here.
@admin.register(Master)
class Master(admin.ModelAdmin):
    list_display = ('name', 'rang', 'phone', 'status')
    list_filter = ('name', 'rang', 'phone', 'status')
