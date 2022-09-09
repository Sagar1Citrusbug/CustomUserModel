from enum import unique
from django import forms

from .models import myUser    
from django.contrib.auth.forms import UserCreationForm


class Register(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text= "required.")
    class Meta:
        model = myUser
        fields = ['name','email','password1','password2']

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
        