from django.shortcuts import render
from .models import Degrees
# Create your views here.
def offer(request):
    carreras = Degrees.objects.all()
    return render(request, 'planes/offer.html',{'carreras':carreras}) 