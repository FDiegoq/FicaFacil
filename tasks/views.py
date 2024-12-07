from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from tasks.models import Tarefa
from users.models import Profile

from .form import taskModelForm
from .form import FilterTask

from django.core.paginator import Paginator

import plotly.express as px
from datetime import datetime
import pytz

# Create your views here.

@login_required(login_url='login')
def home(request):
    user_logado=request.user
    filtertask=FilterTask()
    setor=request.GET.get('setor')
    status=request.GET.get('status')

    if status or setor: ##testa se nao é vazio
        if setor:
            tasks=Tarefa.objects.filter(usuario=user_logado, is_done=False, setor=setor) ##apenas setor
        if status:    
            tasks=Tarefa.objects.filter(usuario=user_logado, is_done=False, status=status) ##apenas status
        if status and setor:
            tasks=Tarefa.objects.filter(usuario=user_logado, is_done=False, status=status, setor=setor) #status e setor
    else:
        tasks = Tarefa.objects.filter(usuario=user_logado, is_done=False) ##Aqui eu estou retornando uma lista de tarefas filtrando por usuário e por tarefa terminada
    
    context={
        'tasks': tasks,
        'user': user_logado,
        'filtertask': filtertask,
    }
    
    return render(request, 'home.html', context)

@login_required
def search_view(request):
    query = request.GET.get('searchbar', '')
    if query:
        tasks = Tarefa.objects.filter(titulo__icontains=query, is_done=False) | Tarefa.objects.filter(descricao__icontains=query, is_done=False)
    else:
        tasks = Tarefa.objects.filter(usuario=request.user, is_done=False) 

    return render(request, 'search.html', {'tasks': tasks, 'query': query})

@login_required
def search_dones(request):
    query = request.GET.get('search', '')
    if query:
        tasks = Tarefa.objects.filter(titulo__icontains=query, is_done=True)
    else:
        tasks=Tarefa.objects.filter(usuario=request.user, is_done=True)

    return render(request, 'search_dones.html', {'tasks': tasks, 'query': query})

@login_required(login_url='login') ##tela pra detalhar as tarefas
def task_details(request, id):
    task=Tarefa.objects.get(id=id)
    
    return render(request, 'task_details.html', {'task':task})

@login_required(login_url='login') ##tela pra editar as tarefas a partir da tela de detalhes
def edit_task(request, id):
    task=Tarefa.objects.get(id=id)
    form=taskModelForm(instance=task)
    if request.method=='POST':
        form=taskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create_task.html', {'form':form})
    

@login_required(login_url='login') ##tela pra excluir as tarefas a partir da tela de detalhes
def delete_task(request, id):
    task=Tarefa.objects.get(id=id)
    task.delete()
    return redirect('home')

@login_required(login_url='login') ####Tela para criar novas tarefas
def create_task(request):
    try:
        perfil_logado=Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
       return HttpResponse('Você não possui um perfil associado. Complete seu perfil para habilitar a criação de tarefas.')
    
    form=taskModelForm(empresa=perfil_logado.empresa)
    if request.method=='POST':
        form=taskModelForm(request.POST, empresa=perfil_logado.empresa)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'create_task.html', {'form':form})

@login_required(login_url='login') ###URL que finaliza tarefas
def finish_task(request, id):
    task=Tarefa.objects.get(id=id)
    task.is_done=True
    task.status='Finalizada'
    task.data_conclusao=datetime.now().astimezone(pytz.timezone('America/Sao_Paulo'))
    task.save()
    return redirect('home')

@login_required(login_url='login')
def restore_task(request, id): ####URL QUE VAI RESTAURAR AS TAREFAS
    task=Tarefa.objects.get(id=id)
    task.is_done=False
    task.status='Pendente'
    task.save()
    return redirect('home')

@login_required(login_url='login') ###TELA DE TAREFAS FINALIZADAS
def done_tasks(request):
    tasks=Tarefa.objects.filter(usuario=request.user, is_done=True)
    paginator=Paginator(tasks, 3)
    page = request.GET.get('page', 1)
    tasks = paginator.page(page)
    return render(request, 'done_tasks.html', {'tasks':tasks})

@login_required(login_url='login')
def profile(request):
    tasks=Tarefa.objects.filter(usuario=request.user, is_done=True)
    
    try:
        perfil_logado=Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
       return HttpResponse('Você não possui um perfil associado. Complete seu perfil para acessar essa página')

    

    return render(request, 'profile.html')

@login_required(login_url='login')
def dashboard(request):
    concluidas=Tarefa.objects.filter(usuario=request.user, is_done=True).count()
    bloqueadas=Tarefa.objects.filter(usuario=request.user, status='Bloqueada').count()
    do_setor=Tarefa.objects.filter(usuario=request.user, setor=request.user.profile.setor, is_done=False,).count()
    para_voce=Tarefa.objects.filter(usuario=request.user, is_done=False).count()

    contexto={
        'concluidas': concluidas,
        'bloqueadas': bloqueadas,
        'do_setor' : do_setor,
        'para_voce': para_voce
 
    }

    return render(request, 'dashboard.html', contexto)


