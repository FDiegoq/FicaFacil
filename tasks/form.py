from django import forms
from tasks.models import Tarefa

class taskModelForm(forms.ModelForm):
    class Meta():
        model=Tarefa
        fields='__all__'
        widgets={
                'titulo': forms.TextInput(attrs={
                'class': 'p-3 bg-neutral-900 w-auto rounded-lg shadow-md text-white',
                'placeholder' : 'Digite o título da tarefa'
            }),
                'descricao': forms.Textarea(attrs={
                'class': 'p-3 bg-neutral-900 w-auto rounded-lg shadow-md text-white',
                'placeholder' : 'Detalhe a descrição da tarefa'
            }),
                'status': forms.Select(attrs={
                'class': 'p-2 bg-neutral-900 w-auto rounded-lg shadow-md text-white',
                'placeholder' : 'Status da tarefa'
            }),
                'setor': forms.Select(attrs={
                'class': 'p-2 bg-neutral-900 w-auto rounded-lg shadow-md text-white',
                'placeholder' : 'Digite seu nome de usuário'
            }),
                'usuario': forms.Select(attrs={
                'class': 'p-2 bg-neutral-900 w-auto rounded-lg shadow-md text-white',
                'placeholder' : 'Digite seu nome de usuário'
            })
        }