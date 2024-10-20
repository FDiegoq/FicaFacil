from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Tarefa
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
    ...

@login_required(login_url='login') ##tela pra excluir as tarefas a partir da tela de detalhes
def delete_task(request, id):
    ...

@login_required(login_url='login')
def create_task(request):
    form=taskModelForm()
    if request.method=='POST':
        form=taskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=taskModelForm()
        
    return render(request,'create_task.html', {'form':form})

@login_required(login_url='login')
def finish_task(request, id):
    task=Tarefa.objects.get(id=id)
    task.is_done=True
    task.status='Finalizada'
    task.save()
    return redirect('home')

@login_required(login_url='login')
def done_tasks(request):
    tasks=Tarefa.objects.filter(usuario=request.user, is_done=True)
    return render(request, 'done_tasks.html', {'tasks':tasks})

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')