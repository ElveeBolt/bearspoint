from django import forms
from .models import Master, Calendar
from service.models import Service


class MasterForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя мастера:',
        required=True,
        help_text='Укажите имя мастера.',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя...'
            }
        )
    )
    rang = forms.ChoiceField(
        label='Ранг мастера:',
        required=False,
        choices=Master.RANG_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Укажите ранг...'
            }
        )
    )
    phone = forms.IntegerField(
        label='Телефон:',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите телефон мастера...'
            }
        )
    )
    status = forms.ChoiceField(
        label='Статус:',
        required=False,
        choices=Master.STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Укажите статус...'
            }
        )
    )
    service = forms.ModelMultipleChoiceField(
        label='Статус:',
        required=False,
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'form-check-input',
                'placeholder': 'Укажите статус...'
            }
        )
    )

    class Meta:
        model = Master
        fields = '__all__'


class CalendarForm(forms.ModelForm):
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
        label='Время начала:',
        required=True,
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите время...',
                'type': 'time'
            }
        )
    )
    time_end = forms.TimeField(
        label='Время завершения:',
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
        model = Calendar
        fields = '__all__'
