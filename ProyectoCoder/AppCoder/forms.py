from django import forms
from .models import Profesores, Estudiantes

class CursoFormulario(forms.Form):
    
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()
    
class ProfesoresFormulario(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ['nombre', 'apellido', 'email', 'profesion', 'cursos']
        widgets = {
            'cursos': forms.CheckboxSelectMultiple
        }

class EstudiantesFormulario(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ['nombre', 'apellido', 'email']
        