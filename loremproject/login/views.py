from django.shortcuts import render

# Create your views here.
def logeo(request):
    return render(request, 'login/logeo.html')

def recover(request):
    return render(request, 'login/recover.html')

def registrate(request):
    return render(request, 'login/registrate.html')