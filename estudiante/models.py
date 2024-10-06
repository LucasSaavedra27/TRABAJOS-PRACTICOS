from django.db import models

# Create your models here.
   
class Curso(models.Model):
    nombre = models.CharField(max_length=40,null="false")
    cantidad_horas = models.PositiveIntegerField(null="false")
    
    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40,null="false")
    apellido = models.CharField(max_length=40,null="false")
    edad = models.PositiveIntegerField(null="false")
    nota_curso = models.PositiveIntegerField(null="false")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, default=1)

    def __str__(self):
        return self.nombre