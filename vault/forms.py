from django import forms
from .models import PasswordEntry

class PasswordEntryForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        exclude = ['user']
        widgets = {
            'password': forms.PasswordInput()
        }
