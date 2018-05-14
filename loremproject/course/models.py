from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from sales.models import Sales

# Create your models here.
class Buy(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=50)
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="courses", null=True, blank=True)
    price = models.DecimalField(verbose_name="Precio", max_digits=6, decimal_places=2)
    quota = models.SmallIntegerField(verbose_name="Cupo", default=0)
    start = models.DateTimeField(verbose_name="Fecha de inicio", default=timezone.now)
    selected = models.BooleanField(verbose_name="Seleccionado",default="False")
    oferta = models.ForeignKey(Sales, verbose_name="Oferta", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ['title']

    def __str__(self):
        return self.title

class ListaCursos(models.Model):
    cliente = models.ForeignKey(User, verbose_name="Cliente", on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Buy, verbose_name="Cursos", related_name="anadirCarrito")
    
    class Meta:
        verbose_name = "lista_curso"
        verbose_name_plural = "lista_cursos"
        ordering = ['cliente']

    def __str__(self):
        return str(self.cliente)