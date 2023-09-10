from django.urls import path
from .views import *

urlpatterns = [
    path('agrega_curso/<nombre>/<camada>', curso),
    path('lista-cursos/', listar_cursos, name='ListaCursos'),
    path('lista-profesores/', listar_profesores, name='ListaProfesores'),
    path('lista-estudiantes/', listar_estudiantes, name='ListaEstudiante'),
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('curso-Formulario/', cursoFormulario, name='CursoFormulario'),
    path('profesores-Formulario/', profesoresFormulario, name='ProfesoresFormulario'),
    path('estudiantes-Formulario/', estudiantesFormulario, name='EstudiantesFormulario'),
    path('busqueda-Camada/', busquedaCamada, name='BusquedaCamada'),
    path('buscar/', buscar, name='Buscar'),
    
]
