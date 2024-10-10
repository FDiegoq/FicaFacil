from django import forms
from tasks.models import Tarefa

class taskModelForm(forms.ModelForm):
    class Meta():
        model=Tarefa
        fields='__all__'
        widgets={

        }