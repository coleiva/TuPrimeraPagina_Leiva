from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar/', views.agregar_juego, name='agregar_juego'),
    path('buscar/', views.buscar_juego, name='buscar_juego'),
]