from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput
from django.forms.widgets import EmailInput
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email']

        labels = {"id_password1": "", "id_password2": '',
                  'last_name': '', 'username': '', 'email': ''}
        widgets = {'password': forms.PasswordInput(
            attrs={'placeholder': 'mot de passe'}),
                   'username': TextInput(attrs={'placeholder': 'pseudo'}),
                   'last_name': TextInput(attrs={'placeholder': 'prénom'}),
                   'email': EmailInput(attrs={'placeholder': 'email'}),
                   }


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {"password": "", "email": ""}
        widgets = {'password': forms.PasswordInput(
            attrs={'placeholder': 'mot de passe'}),
                   'email': EmailInput(attrs={'placeholder': 'email'}),
                   }
