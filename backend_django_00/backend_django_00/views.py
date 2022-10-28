from datetime import datetime
from django.http import HttpRequest, HttpResponse
# request: realiza peticiones
#http response : envia respuiesta con http

def bienvenida(request):
    return HttpResponse("Bienvenido, esto es una vista")

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria="tercera edad"
        else:
            categoria="adultez"
    else:
        if edad < 10:
            categoria = "infancia"
        else:
            categoria = "adolescencia"
    resultado = "<h1> Categoria de la edad: %s</h1>" %categoria
    return HttpResponse(resultado)

def obtenerActual(request):
    r = "<h1>Momento Actual: {} </h1>".format(datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(r)