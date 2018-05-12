from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def mision(request):
    return render(request, 'core/mision.html')

def vision(request):
    return render(request, 'core/vision.html')

def history(request):
    return render(request, 'core/history.html')

def campus(request):
    return render(request, 'core/campus.html')

def about(request):
    return render(request, 'core/about.html')