from django.contrib import admin
from .models import Curso, Entregable, Profesor,Estudiante

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'camada', 'fecha_creacion']
    search_fields= ['nombre', 'camada', 'fecha_creacion']
    list_filter= ['nombre']

class EstudianteAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido','email']
    search_fields=['nombre', 'apellido','email']
    list_filter=['email']

class ProfesorAdmin(admin.ModelAdmin):
    list_display=['nombre', 'apellido','email','profesion']
    search_fields=['nombre', 'apellido','email','profesion']
    list_filter=['email','profesion']

# Register your models here.

admin.site.register(Curso, CursoAdmin)

admin.site.register(Estudiante, EstudianteAdmin)

admin.site.register(Profesor, ProfesorAdmin)

admin.site.register(Entregable)
