from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    return HttpResponse("Soy Pablo - Hola Django - Coder")


def segundaVista(request):
    return HttpResponse("<br>--------------YA SOMOS PROGRAMADORES WEB--------------")


def dia(request):
    variable = datetime.now()
    return HttpResponse(f"Hoy es un gran día<br>{variable}")


def apellido(request, ape):

    fecha = datetime.now()
    return HttpResponse(f"El profe de coder {ape}, es muy bueno..<br><br>...Por lo menos hoy: {fecha}")


def cuantosAniosTengo(request, nac):

    # calcular la edad --- edad

    return HttpResponse("Tu edad es: ")


def probandoTemplate(request):
    miHTML = open(
        "C:/Users/pablo/Desktop/coder/python/Clase 17/Proyecto1/Proyecto1/plantillas/template1.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    # el contexto sirve para mandar datos. En este caso no le estoy pasando nada
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
