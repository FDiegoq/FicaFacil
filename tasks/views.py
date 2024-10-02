from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Tarefa
from users.models import User
# Create your views here.

@login_required(login_url='login')
def home(request):
    user_logado=request.user
    tasks = Tarefa.objects.filter(usuario=user_logado) ##Aqui eu estou retornando uma lista de tarefas filtrando por usuário, apenas pegando tarefas do usuário que está logado, com o dado da request.user
    context={
        'tasks': tasks,
    }
    return render(request, 'home.html', context)