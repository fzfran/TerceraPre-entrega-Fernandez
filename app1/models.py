from django.db import models

# Create your models here.

class Celulares(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    descripcion = models.TextField()
    fecha_de_creacion = models.IntegerField()
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.descripcion} - {self.fecha_de_creacion}'
    
    
class Notebooks(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.TextField()
    fecha_de_creacion = models.IntegerField()
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.fecha_de_creacion}'

class Televisores(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.TextField()
    fecha_de_creacion = models.IntegerField()
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.fecha_de_creacion}'
