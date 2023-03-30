from django import forms
from django.contrib.auth.models import User
from .models import Booking
from service.models import Service
from master.models import Master


class BookingForm(forms.ModelForm):
    master = forms.ModelChoiceField(
        label='Мастер:',
        required=True,
        queryset=Master.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Укажите мастера...'
            }
        )
    )
    service = forms.ModelChoiceField(
        label='Услуга:',
        required=True,
        queryset=Service.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Укажите услугу...'
            }
        )
    )
    user = forms.ModelChoiceField(
        label='Пользователь:',
        required=True,
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Укажите пользователя...'
            }
        )
    )
    date = forms.DateField(
        label='Дата:',
        required=True,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите дату...',
                'type': 'date'
            }
        )
    )
    time_start = forms.TimeField(
        label='Время:',
        required=True,
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите время...',
                'type': 'time'
            }
        )
    )

    class Meta:
        model = Booking
        fields = '__all__'
