from django.db import models
from django.utils import timezone


# Create your models here.
class Sales(models.Model):
    descuento = models.IntegerField(verbose_name="Descuento")
    fecha_inicio = models.DateTimeField(verbose_name="Fecha de inicio", default=timezone.now)
    fecha_fin = models.DateTimeField(verbose_name="Fecha fin", default=timezone.now)

    class Meta:
        verbose_name = "oferta"
        verbose_name_plural = "ofertas"
        ordering = ['id']

    def __str__(self):
        return str(self.descuento) + "%"