from django.urls import path
from .views import generacion_view
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('categoria',views.categoria, name='categoria'),
    path('consejos',views.consejos, name='consejos'),
    path('generacion',views.generacion, name='generacion'),
    path('login',views.login, name='login'),
    path('Registro',views.Registro, name='Registro'),
    path('lista',views.lista, name='lista'),
    path('lista/<str:pk>/<str:action>/', views.lista, name='lista_action'),
    path('generacion/', generacion_view, name='generacion'),
    
    ]