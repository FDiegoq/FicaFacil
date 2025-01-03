from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    pfp=models.ImageField(upload_to='pfps/', blank=True, null=True)
    empresa = models.ForeignKey('tasks.Empresa', on_delete=models.CASCADE, null=False, blank=False)
    setor=models.ForeignKey('tasks.Setor', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.user.username