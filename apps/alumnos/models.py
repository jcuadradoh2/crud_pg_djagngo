from django.db import models

class Alumno(models.Model):
    gen = (('M', 'Masculino'),('F', 'Femenino'),('X', 'GLBTI+'))
    cedula = models.CharField('Cedula', max_length=10)
    nombre = models.CharField('Nombre', null=True, blank=True, max_length=50)
    apellido = models.CharField('Apellido', null=True, blank=True, max_length=50)
    genero = models.CharField('Genero', choices=gen, max_length=1, default='M')
    foto = models.ImageField('Foto', null=True, blank=True, upload_to='img/')

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):    
        return self.nombre



