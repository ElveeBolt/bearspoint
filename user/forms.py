from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин...'
            }
        )
    )
    password = forms.CharField(
        label='Пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль...'
            }
        )
    )


class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='Логин:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин...'
            }
        )
    )
    email = forms.CharField(
        label='E-mail:',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите e-mail...'
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль...'
            }
        )
    )
    password2 = forms.CharField(
        label='Повторите пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль...'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
