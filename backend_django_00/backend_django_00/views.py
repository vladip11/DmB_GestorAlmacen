from django.http import HttpRequest, HttpResponse
# request: realiza peticiones
#http response : envia respuiesta con http

def bienvenida(request):
    return HttpResponse("Bienvenido, esto es una vista")
