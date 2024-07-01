from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'image': forms.FileInput(),
            'phone' : forms.TextInput(attrs={'placeholder': '123456789', 'class': "!text-sm"}),
            'city' : forms.TextInput(attrs={'placeholder': 'Brno', 'class': "!text-sm"}),
            'street' : forms.TextInput(attrs={'placeholder': 'Marianské náměstí 18', 'class': "!text-sm"}),
            'zip' : forms.TextInput(attrs={'placeholder': '637 12', 'class': "!text-sm"}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]