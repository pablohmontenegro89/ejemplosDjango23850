from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estadio, Equipo
from AppCoder.forms import EstadioFormulario

# Create your views here.

# Primer vista


def busquedaEquipo(request):
    return render(request, 'AppCoder/busquedaEquipo.html')


def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        equipo = Equipo.objects.filter(nombre__icontains=nombre)
        #respuesta = f"ESTOY BUSCANDO A :{request.GET['nombre']}"

        # el diccionario lo agregué yo
        return render(request, "AppCoder/resultadoBusqueda.html", {"nombre": equipo.nombre, "ciudad": equipo.ciudad})
    else:
        respuesta = "Che, mandame información"
    return HttpResponse(respuesta)


def estadioFormulario(request):
    # obtiene la dirección y el anioFund

    if request.method == "POST":
        miFormulario = EstadioFormulario(request.POST)
        if miFormulario.is_valid():  # va con ()
            informacion = miFormulario.cleaned_data  # va sin () creo
            estadioInsta = Estadio(
                direccion=informacion["direccion"], anioFund=informacion["anioFund"])
            estadioInsta.save()  # guarda en bd
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = EstadioFormulario()
    # return HttpResponse("Esto es una prueba de inicio")
    return render(request, 'AppCoder/estadioFormulario.html', {"miFormulario": miFormulario})


def inicio(request):
    # return HttpResponse("Esto es una prueba de inicio")
    return render(request, 'AppCoder/inicio.html')


def jugadores(request):
    return render(request, 'AppCoder/jugadores.html')


def equipos(request):
    return render(request, 'AppCoder/equipos.html')
