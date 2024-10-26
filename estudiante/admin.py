# admin.py
from django.contrib import admin
from .models import Estudiante, Curso

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','curso')  
    search_fields = ('nombre', 'apellido') 

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_horas')  
    search_fields = ('nombre', 'cantidad_horas')
