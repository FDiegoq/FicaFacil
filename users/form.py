from django import forms
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta():
        model=User
        fields='__all__'
        widgets={
            'username': forms.TextInput(attrs={
                'class': '',
                'placeholder' : 'Digite seu nome de usuário'
            })
        }