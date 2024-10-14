from django.shortcuts import render, get_object_or_404

from estudiante.models import Estudiante, Curso

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante/listar_estudiantes.html', {'estudiantes': estudiantes})

def mayores_de(request,edad):
    estudiantes = Estudiante.objects.filter(edad__gt=edad)
    return render(request, 'estudiante/mayores_de.html', {'estudiantes': estudiantes, 'edad':edad})

def curso_especifico(request,curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    # Obtener los estudiantes inscritos en ese curso
    estudiantes = curso.estudiante_set.all()
    return render(request, 'estudiante/curso_especifico.html', {'curso': curso, 'estudiantes': estudiantes,'curso_id':curso_id})