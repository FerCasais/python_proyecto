from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from control_studio.models import Estudiante, Curso, Profesor

from django.db.models import Q

from control_studio.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario






# Create your views here.

def listar_estudiantes(request):
    contexto = {
            "estudiantes": Estudiante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="lista_estudiantes.html",
        context=contexto,
    )
    return http_response



def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
      }
    http_response = render(
        request=request,
        template_name="lista_cursos.html",
        context=contexto,
    )
    return http_response

def listar_profesores(request):
    contexto = {
            "profesores": Profesor.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="lista_profesores.html",
        context=contexto,
    )
    return http_response


def crearCurso(request):
   if request.method == "POST":
       data = request.POST
       curso = Curso(nombre=data['nombre'], comision=data['comision'])
       curso.save()
       url_exitosa = reverse('lista_cursos')
       return redirect(url_exitosa)
   else:  # GET
       return render(
           request=request,
           template_name='crear_curso.html',
       )
   
def crearProfesor(request):
   if request.method == "POST":
       data = request.POST
       profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'])
       profesor.save()
       url_exitosa = reverse('lista_profesores')
       return redirect(url_exitosa)
   else:  # GET
       return render(
           request=request,
           template_name='crear_profesor.html',
       )
   
def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        # cursos = Curso.objects.filter(comision__contains=busqueda)
        # Ejemplo filtro avanzado
        cursos = Curso.objects.filter(
            Q(nombre__icontains=busqueda) | Q(comision__contains=busqueda)
        )

        contexto = {
            "cursos": cursos,
        }
        http_response = render(
            request=request,
            template_name='lista_cursos.html',
            context=contexto,
        )
        return http_response
    
   
def crearEstudiante(request):
   if request.method == "POST":
       data = request.POST
       estudiante = Estudiante(nombre=data['nombre'], apellido=data['apellido'])
       estudiante.save()
       url_exitosa = reverse('lista_estudiantes')
       return redirect(url_exitosa)
   else:  # GET
       return render(
           request=request,
           template_name='crear_estudiante.html',
       )
   

   
   