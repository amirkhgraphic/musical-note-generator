from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'avatar',
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'avatar',
            'username',
            'first_name',
            'last_name',
            'email',
        ]
