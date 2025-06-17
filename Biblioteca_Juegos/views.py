from django.shortcuts import render, redirect
from .forms import *
from .models import *


def home(request):
    form = BusquedaForm()
    return render(request, 'Biblioteca_Juegos/home.html', {'form': form})


def agregar_juego(request):
    return render(request, 'Biblioteca_Juegos/seleccionar_juego.html')


def agregar_juego_pc(request):
    mensaje = ""
    if request.method == "POST":
        pc_form = JuegoPCForm(request.POST,request.FILES, prefix="pc")
        if pc_form.is_valid():
            pc_form.save()
            mensaje = "Juego de PC guardado correctamente."
    else:
        pc_form = JuegoPCForm(prefix="pc")

    return render(request, 'Biblioteca_Juegos/formulario_pc.html', {
        'pc_form': pc_form,
        'mensaje': mensaje
    })


def agregar_juego_nintendo(request):
    mensaje = ""
    if request.method == "POST":
        nintendo_form = JuegoNintendoForm(request.POST,request.FILES, prefix="nintendo")
        if nintendo_form.is_valid():
            nintendo_form.save()
            mensaje = "Juego de Nintendo guardado correctamente."
    else:
        nintendo_form = JuegoNintendoForm(prefix="nintendo")

    return render(request, 'Biblioteca_Juegos/formulario_nintendo.html', {
        'nintendo_form': nintendo_form,
        'mensaje': mensaje
    })


def agregar_juego_sony(request):
    mensaje = ""
    if request.method == "POST":
        sony_form = JuegoSonyForm(request.POST,request.FILES, prefix="sony")
        if sony_form.is_valid():
            sony_form.save()
            mensaje = "Juego de Sony guardado correctamente."
    else:
        sony_form = JuegoSonyForm(prefix="sony")

    return render(request, 'Biblioteca_Juegos/formulario_sony.html', {
        'sony_form': sony_form,
        'mensaje': mensaje
    })


def buscar_juego(request):
    resultados = []
    if request.method == "GET":
        form = BusquedaForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados += list(JuegoPC.objects.filter(nombre__icontains=nombre))
            resultados += list(JuegoNintendo.objects.filter(nombre__icontains=nombre))
            resultados += list(JuegoSony.objects.filter(nombre__icontains=nombre))
    return render(request, 'Biblioteca_Juegos/resultados_busqueda.html', {'resultados': resultados})