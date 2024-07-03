from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','email']
        labels = {
            'image': 'Avatar',
            'first_name': 'Jméno',
            'last_name': 'Přijímení',
            'phone': 'Telefon',
            'city': 'Město',
            'street': 'Ulice',
            'zip': 'Psč',
        }
        widgets = {
            'image': forms.FileInput(attrs={'class':"bg-blue-200 rounded-xl mb-2 mx-auto flex"}),
            'first_name' : forms.TextInput(attrs={'class':"bg-blue-200 rounded-xl px-2 py-1 mx-auto text-center mb-2 flex"}),
            'last_name' : forms.TextInput(attrs={'class':"bg-blue-200 rounded-xl px-2 py-1 mx-auto text-center mb-2 flex"}),
            'phone' : forms.TextInput(attrs={'class':"bg-blue-200 rounded-xl px-2 py-1 mx-auto text-center mb-2 flex"}),
            'city' : forms.TextInput(attrs={'class':"bg-blue-200 rounded-xl px-2 py-1 mx-auto text-center mb-2 flex"}),
            'street' : forms.TextInput(attrs={'class':"bg-blue-200 rounded-xl px-2 py-1 mx-auto text-center mb-2 flex"}),
            'zip' : forms.TextInput(attrs={'class':"bg-blue-200 rounded-xl px-2 py-1 mx-auto text-center mb-2 flex"}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]