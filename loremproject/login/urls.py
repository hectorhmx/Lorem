from django.urls import path
from . import views

urlpatterns = [
    path('', views.logeo, name="login"),
    path('registrate/', views.registrate, name="registrate"),
    path('recover/', views.recover, name="recover"),
]