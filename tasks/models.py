from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Empresa(models.Model):
    nome=models.CharField(max_length=340, blank=False, null=False)
    titular=models.CharField(max_length=250, blank=False, null=False)
    regime=models.CharField(max_length=120, blank=False, null=False)
    email=models.EmailField(blank=False, null=False)
    data_abertura=models.DateField(blank=False, null=False)

    def __str__(self):
        return self.nome

class Setor(models.Model):
    nome=models.CharField(max_length=120, blank=False, null=False)
    descricao=models.TextField(blank=False, null=False)
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.nome

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
    usuario=models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    data_criacao=models.DateTimeField(auto_now_add=True)
    is_done=models.BooleanField(default=False ,null=False, blank=False)

    def __str__(self):
        return self.titulo