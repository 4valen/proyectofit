from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Datos, Genero
from django.http import JsonResponse
# Create your views here.


def index(request):
    context = {}
    return render(request, 'fitness/index.html', context)


def layout(request):
    context = {}
    return render(request, 'fitness/layout.html', context)

def categoria(request):
    context = {}
    return render(request, 'fitness/categoria.html', context)


def consejos(request):
    context = {}
    return render(request, 'fitness/consejos.html', context)

def generacion(request):
    context = {}
    return render(request, 'fitness/generacion.html', context)

def generacion_view(request):
    if request.method == 'POST':
        # Procesa la solicitud POST
        fecha_nacimiento = request.POST.get('fechaNacimiento')
        if fecha_nacimiento:
            # Calcula la generación basado en la fecha de nacimiento
            anio = int(fecha_nacimiento.split('-')[0])
            if 1946 <= anio <= 1964:
                generacion = "Baby Boomer"
            elif 1965 <= anio <= 1980:
                generacion = "Generación X"
            elif 1981 <= anio <= 1996:
                generacion = "Millennials"
            elif 1997 <= anio <= 2012:
                generacion = "Generación Z"
            else:
                generacion = "No definido"
            
            return JsonResponse({'generacion': generacion})
        else:
            return JsonResponse({'error': 'Fecha de nacimiento no proporcionada'}, status=400)

    # Para la solicitud GET, simplemente renderiza la plantilla
    return render(request, 'fitness/generacion.html')

def login(request):
    context = {}
    return render(request, 'fitness/login.html', context)

def Registro(request):
    context = {}
    return render(request, 'fitness/Registro.html', context)
""" 
def lista(request):
    v=Datos.objects.all()
    context = {"Datos":v}
    return render(request, 'fitness/lista.html', context) """

def lista(request, pk=None, action=None):
    if pk and action:
        objeto = get_object_or_404(Datos, pk=pk)
        if action == 'delete':
            if request.method == 'POST':
                objeto.delete()
                return redirect('lista')
            context = {
                "Datos": Datos.objects.all(),
                "action": "delete",
                "objeto": objeto
            }
            return render(request, 'fitness/lista.html', context)
        elif action == 'edit':
            if request.method == 'POST':
                # Actualiza los campos del objeto según los datos del formulario
                objeto.nombre = request.POST.get('nombre')
                # Añade más campos aquí según tu modelo
                objeto.save()
                return redirect('lista')
            context = {
                "Datos": Datos.objects.all(),
                "action": "edit",
                "objeto": objeto
            }
            return render(request, 'fitness/lista.html', context)
        elif action == 'add':
            if request.method == 'POST':
                # Crea los campos del objeto según los datos del formulario
                objeto.nombre = request.POST.get('nombre')
                # Añade más campos aquí según tu modelo
                objeto.save()
                return redirect('lista')
            context = {
                "Datos": Datos.objects.all(),
                "action": "add",
                "objeto": objeto
            }
            return render(request, 'fitness/lista.html', context)
        
    else:
        context = {
            "Datos": Datos.objects.all()
        }
        return render(request, 'fitness/lista.html', context)