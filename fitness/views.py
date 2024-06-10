from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {}
    return render(request, 'fitness/index.html', context)

def categoria(request):
    context = {}
    return render(request, 'fitness/categoria.html', context)



def consejos(request):
    context = {}
    return render(request, 'fitness/consejos.html', context)

def generacion(request):
    context = {}
    return render(request, 'fitness/generacion.html', context)

def login(request):
    context = {}
    return render(request, 'fitness/login.html', context)

def Registro(request):
    context = {}
    return render(request, 'fitness/Registro.html', context)

