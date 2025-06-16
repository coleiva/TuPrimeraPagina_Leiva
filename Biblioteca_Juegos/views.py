from django.shortcuts import render, redirect
from .forms import *
from .models import *


def home(request):
    form = BusquedaForm()
    return render(request, 'Biblioteca_Juegos/home.html', {'form': form})


def agregar_juego(request):
    mensaje = ""
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "pc":
            pc_form = JuegoPCForm(request.POST, prefix="pc")
            if pc_form.is_valid():
                pc_form.save()
                mensaje = "Juego de PC guardado correctamente."
        else:
            pc_form = JuegoPCForm(prefix="pc")

        if form_type == "nintendo":
            nintendo_form = JuegoNintendoForm(request.POST, prefix="nintendo")
            if nintendo_form.is_valid():
                nintendo_form.save()
                mensaje = "Juego de Nintendo guardado correctamente."
        else:
            nintendo_form = JuegoNintendoForm(prefix="nintendo")

        if form_type == "sony":
            sony_form = JuegoSonyForm(request.POST, prefix="sony")
            if sony_form.is_valid():
                sony_form.save()
                mensaje = "Juego de Sony guardado correctamente."
        else:
            sony_form = JuegoSonyForm(prefix="sony")
    else:
        pc_form = JuegoPCForm(prefix="pc")
        nintendo_form = JuegoNintendoForm(prefix="nintendo")
        sony_form = JuegoSonyForm(prefix="sony")

    return render(request, 'Biblioteca_Juegos/agregar_juego.html', {
        'pc_form': pc_form,
        'nintendo_form': nintendo_form,
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