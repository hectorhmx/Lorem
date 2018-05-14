from django.contrib import admin
from .models import Sales

# Register your models here.
class SalesAdmin(admin.ModelAdmin):
    list_display = ('id','descuento', 'fecha_inicio', 'fecha_fin')

admin.site.register(Sales, SalesAdmin)