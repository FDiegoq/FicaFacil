from django import forms
from tasks.models import Tarefa
from django.contrib.auth.models import User


class taskModelForm(forms.ModelForm):
    class Meta():
        model=Tarefa
        fields='__all__'
        widgets={
                'titulo': forms.TextInput(attrs={
                'class': 'p-3 bg-neutral-900 w-auto rounded-lg text-white',
                'placeholder' : 'Digite o título da tarefa'
            }),
                'descricao': forms.Textarea(attrs={
                'class': 'p-3 bg-neutral-900 w-auto rounded-lg text-white',
                'placeholder' : 'Detalhe a descrição da tarefa'
            }),
                'status': forms.Select(attrs={
                'class': 'p-2 bg-neutral-900 w-auto rounded-lg text-white',
                'placeholder' : 'Status da tarefa'
            }),
                'setor': forms.Select(attrs={
                'class': 'p-2 bg-neutral-900 w-auto rounded-lg text-white',
                'placeholder' : 'Digite seu nome de usuário'
            }),
                'usuario': forms.Select(attrs={
                'class': 'p-2 bg-neutral-900 w-auto rounded-lg text-white',
                'placeholder' : 'Digite seu nome de usuário'
            })
        }
    def __init__(self, *args, **kwargs):
        empresa = kwargs.pop('empresa', None)
        super().__init__(*args, **kwargs)
        if empresa:
            self.fields['usuario'].queryset = User.objects.filter(profile__empresa=empresa)
class FilterTask(forms.ModelForm):
    class Meta():
        model=Tarefa
        fields=['status', 'setor', 'usuario']
        widgets={
            'setor':forms.Select(attrs={'class':'bg-neutral-800 text-white rounded-md p-1', 'name':'setor'}),
            'status':forms.Select( attrs={'class':'bg-neutral-800 text-white rounded-md p-1', 'status':'status'}),
        }
    def __init__(self, *args, **kwargs):
        super(FilterTask, self).__init__(*args, **kwargs)
        self.fields['status'].required = False
        self.fields['setor'].required = False

