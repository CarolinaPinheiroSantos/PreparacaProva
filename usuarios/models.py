from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAbs(AbstractUser):
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.username
    
class Usuario(models.Model):
    class Meta:
        db_table = 'usuarios_usuario'
