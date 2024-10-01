from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Tarefa
# Create your views here.

@login_required(login_url='login')
def home(request):
    tasks=Tarefa.objects.all()
    context={
        'tasks': tasks
    }
    return render(request, 'home.html', context)