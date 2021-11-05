from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email']

        labels = {"password": "Mot de passe",
                  'last_name': 'Prénom', 'username': 'pseudo'}
        widgets = {"password": forms.PasswordInput()}


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        labels = {"password": "Mot de passe", "username": "pseudo"}
        widgets = {"password": forms.PasswordInput()}
