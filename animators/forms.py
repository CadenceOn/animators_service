from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Request

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['description', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }