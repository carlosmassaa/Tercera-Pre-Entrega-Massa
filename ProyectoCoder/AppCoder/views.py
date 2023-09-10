from django.shortcuts import render
from .models import Curso, Profesores, Estudiantes
from django.http import HttpResponse, HttpRequest
from .forms import CursoFormulario, ProfesoresFormulario, EstudiantesFormulario

# Create your views here.
def curso (req, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse(f""" <P> Curso: {curso.nombre} - Camada: {curso.camada} creado con éxito!<P>""")

def listar_cursos(req):

    lista = Curso.objects.all()
    
    return render(req, "lista_cursos.html", {"lista_cursos":lista})

def inicio(req):
    
    return render(req, 'inicio.html')
    return HttpResponse("Vista de Inicio")

def cursos(req):
    return render(req, 'cursos.html')
    return HttpResponse("Vista de Cursos")


def cursoFormulario(req):
    
    print('method', req.method)
    print('method', req.POST)
    if req.method == 'POST':
        
        miFormulario = CursoFormulario(req.POST)
    
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            curso = Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()
            return render(req, "inicio.html")
        
    else:
        miFormulario = CursoFormulario()
        return render(req, "cursoFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(req):
    return render(req, "busquedaCamada.html")

def buscar(req: HttpRequest):
    
    if req.GET["camada"]:
        camada = req.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(req, "resultadosBusqueda.html", {'cursos': cursos})

    else: 
        return HttpResponse(f"Debe agregar una camada")
        
        

def profesores(req):
    return render(req, 'profesores.html')
    return HttpResponse("Vista de Profesores")


from .forms import ProfesoresFormulario

def profesoresFormulario(req):
    if req.method == 'POST':
        miFormulario = ProfesoresFormulario(req.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(req, "inicio.html")
    else:
        miFormulario = ProfesoresFormulario()
    return render(req, "profesoresFormulario.html", {"miFormulario": miFormulario})

def listar_profesores(req):

    lista = Profesores.objects.all()
    
    return render(req, "lista_profesores.html", {"lista_profesores":lista})










def estudiantes(req):
    return render(req, 'estudiantes.html')
    return HttpResponse("Vista de Estudiantes")

def listar_estudiantes(req):

    lista = Estudiantes.objects.all()
    
    return render(req, "lista_estudiantes.html", {"lista_estudiante":lista})

def estudiantesFormulario(req):
    if req.method == 'POST':
        miFormulario = EstudiantesFormulario(req.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(req, "inicio.html")
    else:
        miFormulario = EstudiantesFormulario()
    return render(req, "estudiantesFormulario.html", {"miFormulario": miFormulario})






def entregables(req):
    return render(req, 'entregables.html')  
    return HttpResponse("Vista de Entregables")
