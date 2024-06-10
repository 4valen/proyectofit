from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('categoria',views.categoria, name='categoria'),
    path('consejos',views.consejos, name='consejos'),
    path('generacion',views.generacion, name='generacion'),
    path('login',views.login, name='login'),
    path('Registro',views.Registro, name='Registro'),

    ]