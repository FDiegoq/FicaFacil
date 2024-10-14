from django import forms 
from .models import Profile

class profileModelForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields='__all__'
        widgets={
            'user': forms.Select(attrs={
                'class': 'p-3 bg-stone-900 w-full rounded-lg shadow-md text-white',}
            ),
            'pfp':forms.FileInput(attrs={
                'class': 'p-3 bg-stone-900 w-full rounded-lg shadow-md text-white'
            })


        }