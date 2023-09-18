from django.db import models

# Create your models here.
class Curso(models.Model):
    
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    fecha_creacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.camada} - {self.fecha_creacion}'
    
    class Meta():
        verbose_name = 'Course'
        verbose_name_plural = 'The Courses'
        ordering = ('nombre', '-camada', '-fecha_creacion')
        unique_together = ('nombre', 'camada')


class Estudiante(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email}'
    
    class Meta():
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ('nombre', '-apellido', '-email')
        unique_together = ('nombre', 'apellido', 'email')



class Profesor(models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email} - {self.profesion}'
    
    class Meta():
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ('nombre', '-apellido', '-email', '-profesion')
        unique_together = ('nombre', 'apellido', 'email', 'profesion')



class Entregable(models.Model):

    nombre= models.CharField(max_length=30)
    fechaDeEntrega= models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} - {self.fechaDeEntrega} - {self.entregado}'
    
    class Meta():
        verbose_name = 'Entregable'
        verbose_name_plural = 'Entregables'
        ordering = ('nombre', '-fechaDeEntrega', '-entregado')
        unique_together = ('nombre', 'fechaDeEntrega', 'entregado')

