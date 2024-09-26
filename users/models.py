from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(blank=False, null=False)
    pfp=models.ImageField(upload_to='media/pfps')
    empresa = models.ForeignKey('tasks.Empresa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.email