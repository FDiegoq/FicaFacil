from django import forms
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta():
        model=User
        fields='__all__'
        widgets={
            'username': forms.TextInput(attrs={
                'class': 'p-3 bg-stone-800 w-full rounded-lg shadow-md text-white',
                'placeholder' : 'Digite seu nome de usuário'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'p-3 bg-stone-800 w-full rounded-lg shadow-md text-white',
                'placeholder' : 'Digite seu email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'p-3 bg-stone-800 w-full rounded-lg shadow-md text-white',
                'placeholder' : 'Digite sua senha'
            }),
                'password2': forms.PasswordInput(attrs={
                'class': 'p-3 bg-stone-800 w-full rounded-lg shadow-md text-white',
                'placeholder' : 'Repita a sua senha'
            }),
        }