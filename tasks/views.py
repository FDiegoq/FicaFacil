from django.shortcuts import render, redirect, HttpResponse
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
    
    form=taskModelForm()
    empresa_logada=perfil_logado.empresa
    perfis_da_empresa=Profile.objects.filter(empresa=empresa_logada)
    form.fields['perfil'].queryset=perfis_da_empresa
    if request.method=='POST':
        form=taskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request,'create_task.html', {'form':form})

@login_required(login_url='login') ###URL que finaliza tarefas
def finish_task(request, id):
    task=Tarefa.objects.get(id=id)
    task.is_done=True
    task.status='Finalizada'
    task.save()
    return redirect('home')

def restore_task(request, id): ####URL QUE VAI RESTAURAR AS TAREFAS
    task=Tarefa.objects.get(id=id)
    task.is_done=False
    task.status='Pendente'
    task.save()
    return redirect('home')

@login_required(login_url='login') ###TELA DE TAREFAS FINALIZADAS
def done_tasks(request):
    tasks=Tarefa.objects.filter(usuario=request.user, is_done=True)
    return render(request, 'done_tasks.html', {'tasks':tasks})

@login_required(login_url='login')
def tasks_dashboard(request):
    return render(request, 'tasks_dashboard.html')

@login_required(login_url='login') ##Perfil do usuário
def profile(request):
    return render(request, 'profile.html')