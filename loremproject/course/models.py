from django.db import models
from django.utils import timezone

# Create your models here.
class Buy(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=50)
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="courses", null=True, blank=True)
    price = models.DecimalField(verbose_name="Precio", max_digits=6, decimal_places=2)
    quota = models.SmallIntegerField(verbose_name="Cupo", default=0)
    start = models.DateTimeField(verbose_name="Fecha de inicio", default=timezone.now)

    class Meta:
        verbose_name = "compra"
        verbose_name_plural = "compras"
        ordering = ['title']

    def __str__(self):
        return self.title