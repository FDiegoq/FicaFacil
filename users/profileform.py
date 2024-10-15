from django import forms 
from .models import Profile

class profileModelForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields='__all__'
        widgets={
                'pfp':forms.FileInput(attrs={
                'class': 'hidden'
            }),
                'empresa':forms.Select(attrs={
                'class': 'p-3 bg-stone-900 w-full rounded-lg shadow-md text-white'
            }),
                'setor':forms.Select(attrs={
                'class': 'p-3 bg-stone-900 w-full rounded-lg shadow-md text-white'
            }),


        }