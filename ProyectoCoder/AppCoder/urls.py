from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agrega_curso/<nombre>/<camada>', cursos),
    path('lista_cursos', listar_cursos),
    path('', inicio, name="Inicio"), #este era nuestro primer view
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('cursoFormulario/', cursoFormulario, name="CursoFormulario"),
    path('profesoresFormulario/', profesoresFormulario, name="profesoresFormulario"),
    path('estudiantesFormulario/', estudiantesFormulario, name="estudiantesFormulario"),
    path('entregablesFormulario/', entregablesFormulario, name="entregablesFormulario"),
    path('busquedaCamada/', busquedaCamada, name="busquedaCamada"),
    path('buscar/', buscar, name="Buscar"),

]
