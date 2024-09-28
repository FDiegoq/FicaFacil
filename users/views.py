from django.shortcuts import render
from .form import UserModelForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    form=UserModelForm()
    if request.method=='GET':
        form=UserModelForm()


    return render(request, 'signup.html', {'form':form})