from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso,Estudiante,Profesor,Entregable
from AppCoder.forms import CursoFormulario,ProfesorFormulario,EstudianteFormulario,EntregableFormulario

# Create your views here.


def inicio(request):
    context = {'inicio': 'Inicio'}
    return render(request, "inicio.html",context)

def cursos(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
 
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()

            return render(request, "inicio.html")
    else:
    
        miFormulario = CursoFormulario()
 
    return render(request, "cursos.html", {"miFormulario": miFormulario})


def listar_cursos(request):
    lista = Curso.objects.all()
    return render(request, "lista_cursos.html" , {"lista_cursos":lista})

def profesores(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
 
            miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
            
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"],profesion=informacion["profesion"])
                  profesor.save()

            return render(request, "inicio.html")
    else:
    
        miFormulario = ProfesorFormulario()
 
    return render(request, "profesores.html", {"miFormulario": miFormulario})

def estudiantes(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
 
            miFormulario = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html
            
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  entregable = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
                  entregable.save()

            return render(request, "inicio.html")
    else:
    
        miFormulario = EstudianteFormulario()
 
    return render(request, "estudiantes.html", {"miFormulario": miFormulario})

def entregables(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
 
            miFormulario = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
            
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  entregable = Entregable(nombre=informacion["nombre"], fechadeentrega=informacion["fechaDeEntrega"])
                  entregable.save()

            return render(request, "inicio.html")
    else:
    
        miFormulario = EntregableFormulario()
 
    return render(request, "entregables.html", {"miFormulario": miFormulario})

def cursoFormulario(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
 
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()

                  return render(request, "inicio.html")
    else:
    
        miFormulario = CursoFormulario()
 
    return render(request, "cursoFormulario.html", {"miFormulario": miFormulario})

def profesoresFormulario(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
 
                miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
            
 
                if miFormulario.is_valid():
                      informacion = miFormulario.cleaned_data
                      profesores_ = Profesor(nombre=informacion["Nombre"], apellido=informacion["Apellido"], email=informacion["Email"],profesion=informacion["Profesion"])
                      profesores_.save()

                return render(request, "inicio.html")
    else:
    
        miFormulario = ProfesorFormulario()
 
    return render(request, "profesores.html", {"miFormulario": miFormulario})

def estudiantesFormulario(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
 
                miFormulario = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html
            
 
                if miFormulario.is_valid():
                      informacion = miFormulario.cleaned_data
                      estudiantes_ = Estudiante(nombre=informacion["Nombre"], apellido=informacion["Apellido"], email=informacion["Email"])
                      estudiantes_.save()

                return render(request, "inicio.html")
    else:
    
        miFormulario = EstudianteFormulario()
 
    return render(request, "estudiantes.html", {"miFormulario": miFormulario})

def entregablesFormulario(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
 
            miFormulario = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
            
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  entregable = Curso(nombre=informacion["nombre"], fechadeentrega=informacion["fechaDeEntrega"])
                  entregable.save()

            return render(request, "inicio.html")
    else:
    
        miFormulario = EntregableFormulario()
 
    return render(request, "entregables.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

    if request.GET["camada"]:
          
          camada = request.GET['camada']
          cursos = Curso.objects.filter(camada__icontains=camada)

          return render(request, "AppCoder/resultadosBusquedas.html", {"cursos":cursos, "camada":camada})
    
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


