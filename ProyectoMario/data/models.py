from django.db import models

# Create your models here.
class Titulo(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Nombre del título')

    class Meta:
        verbose_name='Titulo'
        verbose_name_plural='Titulos'

    def __str__(self):
        return "%s" % self.titulo

class Proyecto(models.Model):
    proyecto = models.CharField(max_length=100, verbose_name='Nombre del proyecto')
    descripcion = models.TextField(verbose_name='Descripción del Proyecto')
    imagen = models.ImageField(verbose_name='Imagen del Producto Final', upload_to='proyectos/')

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'

    def __str__(self):
        return "%s" % self.proyecto