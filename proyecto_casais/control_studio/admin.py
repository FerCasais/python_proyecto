from django.contrib import admin

# Register your models here.
from control_studio.models import Curso, Estudiante, Profesor

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
