from django import forms

class CursoFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   comision = forms.IntegerField(required=True, max_value=50000)



class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)