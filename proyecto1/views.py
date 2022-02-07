from django.http import HttpResponse
import datetime

from django.template import Template, Context


def saludo(request):
    nombre = "MARÍA"
    fecha_actual = datetime.datetime.now()
    temas_curso = ["Plantillas", "Condicionales", "Bucles"]
    doc_externo = open(r"C:\Users\María Castro\Desktop\TestDjango\proyecto1\templates\index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    cxt = Context({"nombre_usuario": nombre, "fecha": fecha_actual, "temas": temas_curso})
    documento = plt.render(cxt)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Adiós Mundo!")

def dameFecha(request):
    fechaActual = datetime.datetime.now()
    fecha = "<html><body><h2>Fecha Actual: {}</h2></body></html>".format(fechaActual)
    return HttpResponse(fecha)

def calculaEdad(request, edad, agno):
    #edadActual = 30
    periodo = agno-2022
    edad = edad + periodo
    documento = "<html><body><h2>Edad en el año {}: {} años</h2></body></html>".format(agno, edad)
    return HttpResponse(documento)