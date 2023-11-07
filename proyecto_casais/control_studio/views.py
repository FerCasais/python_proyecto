from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def listar_estudiantes(request):
    contexto = {
        "profesor": "Fernando",
        "estudiantes": [
            {"nombre": "Florencia", "apellido": "Lopez", "nota": 4},
            {"nombre": "Vigo", "apellido": "Fernandez", "nota": 10},
            {"nombre": "Azul", "apellido": "Langer", "nota": 6},
            {"nombre": "Pedro", "apellido": "Miranda", "nota": 8},
        ],

    }
    http_response = render(
        request=request,
        template_name="lista_estudiantes.html",
        context=contexto,
    )
    return http_response