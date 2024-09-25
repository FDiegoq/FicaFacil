from django.db import models
from ..users.models import Usuario
# Create your models here.

class Setor(models.Model):
    nome=models.CharField(max_length=120, blank=False, null=False)
    descrição=models.TextField(blank=False, null=False)

class Empresa(models.model):
    nome=models.CharField(max_length=340, blank=False, null=False)
    titular=models.CharField(max_length=250, blank=False, null=False)
    regime=models.CharField(max_lenght=120, blank=False, null=False)
    email=models.EmailField(blank=False, null=False)
    data_abertura=models.DateField(blank=False, null=False)

STATUS_CHOICES=(
    ('Bloqueada')
    ('Pendente')
    ('Em andamento')
    ('Finalizada')

)
class Tarefa(models.Model):
    titulo=models.CharField(max_length=500, blank=False, null=False)
    descricao=models.TextField(blank=False, null=False)
    status=models.CharField(choices=STATUS_CHOICES,blank=False, null=False)
    setor=models.ForeignKey(Setor, on_delete=models.CASCADE, blank=False, null=False)
    usuario=models.ManyToManyField(to=Usuario, blank=False, null=False)
    imagem=models.ImageField(upload_to='Media/Tarefas/', blank=True, null=True)
    data_criacao=models.DateTimeField(auto_now_add=True)
