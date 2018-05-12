from django.db import models

# Create your models here.

class Degrees(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=50)
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="ImgPlanes", null=True, blank=True)
    link = models.URLField(verbose_name="URL",max_length=100)
    clave = models.IntegerField(verbose_name="Clave")

    class Meta:
        verbose_name = "plan_estudio"
        verbose_name_plural = "planes_estudio"
        ordering = ['clave']

    def __str__(self):
        return self.title
