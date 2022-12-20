from django.db import models

# Create your models here.

class usuarioclass(models.Model):
    nombre= models.CharField(max_length=30)
    usuario= models.CharField(max_length=30)
    antiguedad= models.IntegerField()

class moderador(models.Model):
    nombre= models.CharField(max_length=30)
    usuario= models.CharField(max_length=30)
    email= models.EmailField()

class usuario_fiel(models.Model):
    nombre= models.CharField(max_length=30)
    usuario= models.CharField(max_length=30)
    antiguedad= models.IntegerField()