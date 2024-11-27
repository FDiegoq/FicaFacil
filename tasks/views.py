from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from tasks.models import Tarefa
from users.models import Profile
from .form import taskModelForm
from .form import FilterTask
from django.core.paginator import Paginator
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
        tasks = Tarefa.objects.none() 

    return render(request, 'search.html', {'tasks': tasks, 'query': query})

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
def task_filters(request):
    if request.method=='GET': 
        filtradas=Tarefa.objects.filter(titulo='icontais__'),
    return render(request, 'home.html')

@login_required(login_url='login')
def profile(request):

    return render(request, 'profile.html')
