from django import forms
from .models import Master
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
