from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    title = forms.CharField(
        label='Название услуги:',
        required=True,
        help_text='Укажите название услуги.',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите название...'
            }
        )
    )
    description = forms.CharField(
        label='Описание:',
        required=False,
        help_text='Описание услуги',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание к услуге...',
                'rows': 5
            }
        )
    )
    time = forms.IntegerField(
        label='Продолжительность:',
        required=True,
        help_text='Укажите продолжительность услуги в минутах.',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите продолжительность...'
            }
        )
    )
    price = forms.IntegerField(
        label='Цена:',
        required=True,
        help_text='Укажите цену за услугу в гривнах.',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите цену...'
            }
        )
    )

    class Meta:
        model = Service
        fields = '__all__'
