# forms.py
from django import forms
from .models import CustomUser

from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

class CustomLoginForm(AuthenticationForm):
    pass