from django import forms
from django.forms import ModelForm, widgets
from django.forms.fields import EmailField
from .models import User

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['last_name','email', 'password']
        
        labels = {"password":"Mot de passe", 'last_name':'Prénom'}
        widgets = {"password":forms.PasswordInput()}

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        
        labels = {"password":"Mot de passe"}
        widgets = {"password":forms.PasswordInput()}
