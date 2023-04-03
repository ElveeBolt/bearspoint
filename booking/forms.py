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


class BookingServiceForm(forms.ModelForm):
    master = forms.IntegerField(
        label='Мастер:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите мастера...',
                'type': 'hidden'
            }
        )
    )
    service = forms.IntegerField(
        label='Услуга:',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите услугу...'
            }
        )
    )
    user = forms.IntegerField(
        label='Пользователь:',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
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
                'readonly': 'readonly',
                'type': 'date'
            }
        )
    )
    time_start = forms.ChoiceField(
        label='Время:',
        required=True,
        choices=(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Укажите время...'
            }
        )
    )

    def __init__(self, time_start_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time_start'].choices = time_start_choices

    class Meta:
        model = Booking
        fields = '__all__'