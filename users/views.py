from django.shortcuts import render,redirect, HttpResponse
from .form import UserModelForm
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout
from django.contrib.auth.decorators import login_required
from .profileform import profileModelForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    form=UserModelForm()
    if request.method=='GET':
        form=UserModelForm()
    elif request.method=='POST':
        username=request.POST.get('username')
        senha=request.POST.get('password')

        user=authenticate(request, username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('home')
        else:
            HttpResponse('Nome de usuário ou senha incorretos')
    return render(request, 'login.html',{'form':form})

def signup(request):
    form=UserModelForm()
    if request.method=='GET':
        form=UserModelForm()
    elif request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        senha=request.POST.get('password')
            
        user_igual=User.objects.filter(username=username).first()

        if user_igual:
            HttpResponse('Já existe um usuário com esse username')
        else:
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()
            return redirect('login')
    return render(request, 'signup.html', {'form':form})

def exitlogout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def complete_profile(request):
    form=profileModelForm()
    if request.method=="POST":
        form=profileModelForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=request.user
            form.save()
            return redirect('home')
    return render(request, 'complete_profile.html', {'form':form})