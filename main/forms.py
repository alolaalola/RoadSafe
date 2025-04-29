from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Accident

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Электронная почта'
    )
    username = forms.CharField(label='Имя пользователя')


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class AccidentForm(forms.ModelForm):
    class Meta:
        model = Accident
        fields = ['title', 'description', 'accident_type', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput()
        }
        labels = {
            'title': 'Название ДТП',
            'description': 'Описание',
            'accident_type': 'Тип ДТП',
        }
