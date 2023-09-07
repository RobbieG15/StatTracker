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

class OrganizationCreationForm(forms.Form):

    school = forms.CharField(label = "School Name")
    city = forms.CharField(label = "City")
    state = forms.CharField(label = "State")
    org_type = forms.CharField(label = "Org Type")

class TeamCreationForm(forms.Form):
    team_Name = forms.CharField(label = "Team Name")

class PlayerAddForm(forms.Form):
    first_name = forms.CharField(
        label = "First Name"
    )

    last_name = forms.CharField(
        label = 'Last Name'
    )

    number = forms.IntegerField()

class UploadFileForm(forms.Form):
    file = forms.FileField()