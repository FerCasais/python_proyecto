from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    saludo= "hola chicos"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo= f"hola chicos, hoy es día {hoy.day}/ {hoy.month}, hora {hoy. hour}: {hoy.minute} hs."
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

def saludar_con_html(request):
    contexto = {
        "profesor": "Fernando",
        "tutores": ["Mariana", "Florencial", "Vigo", ]

    }
    Http_Response= render(
        request=request,
        template_name='base.html',
        context=contexto)
    return Http_Response