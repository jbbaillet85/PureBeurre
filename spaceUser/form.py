from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email']

        labels = {"password1": "",
                  'last_name': '', 'username': '', 'email':''}
        widgets = {"password": forms.PasswordInput(attrs={'placeholder': 'mot de passe'}),
                   'password': TextInput(attrs={'placeholder': 'mot de passe'}),
                   'username': TextInput(attrs={'placeholder': 'pseudo'}),
                   'last_name': TextInput(attrs={'placeholder': 'prénom'}),
                   'email': TextInput(attrs={'placeholder': 'email'}),
                   }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {"password": "", "username": ""}
        widgets = {"password": forms.PasswordInput(),
                   'username': TextInput(attrs={'placeholder': 'pseudo'}),
                   'password': TextInput(attrs={'placeholder': 'mot de passe'})}
