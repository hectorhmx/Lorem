from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('mision/', views.mision, name="mision"),
    path('vision/', views.vision, name="vision"),
    path('history/', views.history, name="history"),
    path('campus/', views.campus, name="campus"),
    path('about/', views.about, name="about"),
]