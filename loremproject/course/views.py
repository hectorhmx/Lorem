from django.shortcuts import render
from .models import Buy

# Create your views here.
def course(request):
    courses = Buy.objects.all() 
    return render(request, 'course/courses.html', {'courses':courses})