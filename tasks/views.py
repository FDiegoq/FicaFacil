from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Tarefa
from users.models import Profile
# Create your views here.

@login_required(login_url='login')
def home(request):
    user_logado=request.user
    tasks = Tarefa.objects.filter(usuario=user_logado) ##Aqui eu estou retornando uma lista de tarefas filtrando por usuário, apenas pegando tarefas do usuário que está logado, com o dado da request.user
    try:
        profile = Profile.objects.get(user=user_logado) ##teste se o user tem um profile, se não, ele retorna a chave profile vazia
    except Profile.DoesNotExist:
        profile = Profile.objects.filter(user=user_logado)
        profile.empresa='Sem informações'
        profile.setor='Sem informações'   #caso não tenha perfil, seta as informações de setor e empres para a string 'sem informações
    context={
        'tasks': tasks,
        'user': user_logado,
        'profile': profile
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def create_task(request):
    return render(request,'create_task.html')