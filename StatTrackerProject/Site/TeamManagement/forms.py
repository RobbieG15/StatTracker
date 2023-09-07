from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    firstName = forms.CharField(label = 'FirstName')
    lastName = forms.CharField(label = 'Last Name')
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'firstName', 'lastName', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length = 255, widget = forms.PasswordInput)