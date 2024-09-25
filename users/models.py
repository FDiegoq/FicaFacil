from django.db import models
from django.contrib.auth.models import AbstractUserUser
from ..tasks.models import Empresa
# Create your models here.

class Usuario(AbstractUserUser):

    #CAMPOS EXTRAS

    Email=models.EmailField(blank=False, null=False)
    Empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)