from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.comision})"

class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.apellido} ({self.nombre})"

class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega= models.DateTimeField(auto_now_add=True)
    esta_aprobado= models.BooleanField(default=False)
