from django.shortcuts import render, redirect
from .models import Buy,ListaCursos

# Create your views here.
def course(request):
    courses = Buy.objects.all() 
    return render(request, 'course/courses.html', {'courses':courses})
