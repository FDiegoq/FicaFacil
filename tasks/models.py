from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Setor(models.Model):
    nome=models.CharField(max_length=120, blank=False, null=False)
    descrição=models.TextField(blank=False, null=False)

class Empresa(models.Model):
    nome=models.CharField(max_length=340, blank=False, null=False)
    titular=models.CharField(max_length=250, blank=False, null=False)
    regime=models.CharField(max_length=120, blank=False, null=False)
    email=models.EmailField(blank=False, null=False)
    data_abertura=models.DateField(blank=False, null=False)

STATUS_CHOICES=[
    ('Bloqueada', 'Bloqueada'),
    ('Pendente', 'Pendente'),
    ('Em andamento', 'Em andamento'),
    ('Finalizada', 'Finalizada')

]
class Tarefa(models.Model):
    titulo=models.CharField(max_length=500, blank=False, null=False)
    descricao=models.TextField(blank=False, null=False)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,blank=False, null=False)
    setor=models.ForeignKey(Setor, on_delete=models.CASCADE, blank=False, null=False)
    usuario=models.ManyToManyField(User)
    imagem=models.ImageField(upload_to='Media/Tarefas/', blank=True, null=True)
    data_criacao=models.DateTimeField(auto_now_add=True)
