from django import forms
from .models import Usuario

class LoginForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['username','password']
        labels={
            'password': 'Contraseña',
            'username': 'Usuario',
        }