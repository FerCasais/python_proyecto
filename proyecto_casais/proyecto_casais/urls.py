"""
URL configuration for proyecto_casais project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from proyecto_casais.views import saludar_con_fecha
from proyecto_casais.views import saludar_con_html
from control_studio.views import listar_estudiantes, listar_cursos, crearCurso, buscar_cursos, crearEstudiante, listar_profesores, crearProfesor



urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludar_con_fecha),
    path('', saludar_con_html, name="inicio"),
    path('estudiantes/', listar_estudiantes, name="lista_estudiantes"),
    path('cursos/', listar_cursos, name="lista_cursos"),
    path('profesores/', listar_profesores, name="lista_profesores"),
    path('crearCurso/', crearCurso, name="crearCurso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
    path("crearEstudiante/", crearEstudiante, name="crear_estudiante"),
    path("crearProfesor/", crearProfesor, name="crear_profesor"),
   
 
     
   
 
]
