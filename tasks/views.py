from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Tarefa
from users.models import Profile
from .form import taskModelForm
# Create your views here.

@login_required(login_url='login')
def home(request):
    user_logado=request.user
    tasks = Tarefa.objects.filter(usuario=user_logado, is_done=False) ##Aqui eu estou retornando uma lista de tarefas filtrando por usuário e por tarefa terminada
    context={
        'tasks': tasks,
        'user': user_logado,
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def create_task(request):
    form=taskModelForm()
    return render(request,'create_task.html', {'form':form})

def done_tasks(request):
    ...