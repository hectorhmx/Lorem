from django.db import models

# Create your models here.
class Usuario(models.Model):
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    correo = models.CharField(max_length=25)
    rfc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=40)
    telefono=models.CharField(max_length=12)
    admin=models.BooleanField(default=False)