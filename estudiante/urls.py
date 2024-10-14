from django.urls import path
from estudiante import views

app_name = 'estudiante'

urlpatterns = [
    path('listar_estudiantes', views.listar_estudiantes, name='listar_estudiantes'),
    path('mayores_de/<int:edad>/', views.mayores_de, name='mayores_de'),
    path('curso_especifico/<int:curso_id>/', views.curso_especifico, name='curso_especifico'),
]