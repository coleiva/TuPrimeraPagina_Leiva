from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar/', views.agregar_juego, name='agregar_juego'),
    path('agregar/pc', views.agregar_juego_pc, name='agregar_juego_pc'),
    path('agregar/nintendo', views.agregar_juego_nintendo, name='agregar_juego_nintendo'),
    path('agregar/sony', views.agregar_juego_sony, name='agregar_juego_sony'),
    path('buscar/', views.buscar_juego, name='buscar_juego'),
]