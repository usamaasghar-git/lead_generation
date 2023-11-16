from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','role', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
