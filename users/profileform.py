from django import forms 
from .models import Profile

class profileModelForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields=['empresa', 'setor']
        widgets={
                ##'pfp':forms.FileInput(attrs={
                ##'class': 'hidden',
               ## 'id':'pfp'
           # }),
                'empresa':forms.Select(attrs={
                'class': 'p-3 bg-stone-900 w-full rounded-lg shadow-md text-white'
            }),
                'setor':forms.Select(attrs={
                'class': 'p-3 bg-stone-900 w-full rounded-lg shadow-md text-white'
            }),
        }