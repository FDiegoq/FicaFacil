from django import forms
from .models import Tarefa
class TaskModelForm(forms.ModelForm):
    model=Tarefa
    fields='__all__'
    widgets={
        
    }