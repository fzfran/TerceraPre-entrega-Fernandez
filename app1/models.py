from django.db import models

# Create your models here.

class Celulares(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.TextField()
    fecha_de_creacion = models.IntegerField()
    
    
class Notebooks(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.TextField()
    fecha_de_creacion = models.IntegerField()
    
class Televisores(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.TextField()
    fecha_de_creacion = models.IntegerField()