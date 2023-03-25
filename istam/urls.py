"""istam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_istam.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('login/', login_view, name="vista_login"),
    path('inicio/',inicio_view, name="vista_inicio"),
    path('logout/',logout_view,name="vista_logout"),

    path('login/', login_view, name="vista_login"),
    path('inicio/', inicio_view, name="vista_inicio"),
    path('logout/', logout_view, name="vista_logout"),

   path('registrar/',registrar_view, name="vista_registro"),

    #URL CON VISTAS BASADAS EN CLASES
    path('lista_estudiante/', login_required(ListaEstudiante.as_view()), name="listar_estudiante"),
    path('crea_estudiante/',login_required(CrearEstudiante.as_view()), name="crear_estudiante"),
    path('edita_estudiante/<int:pk>/', login_required(ActualizarEstudiante.as_view()), name='editar_estudiante'),
    path('elimina_estudiante/<int:pk>/', login_required(EliminarEstudiante.as_view()), name='eliminar_estudiante'),

    path('lista_matricula/', login_required(ListaMatricula.as_view()), name="listar_matricula"),
    path('crea_matricula/',login_required(CrearMatricula.as_view()), name="crear_matricula"),
    path('edita_matricula/<int:pk>/', login_required(ActualizarMatricula.as_view()), name='editar_matricula'),
    path('elimina_matricula/<int:pk>/', login_required(EliminarEstudiante.as_view()), name='eliminar_matricula'),

    path('lista_carrera/', login_required(ListaCarrera.as_view()), name="listar_carrera"),
    path('crea_carrera/',login_required(CrearCarrera.as_view()), name="crear_carrera"),
    path('edita_carrera/<int:pk>/', login_required(ActualizarCarrera.as_view()), name='editar_carrera'),
    path('elimina_carrera/<int:pk>/', login_required(EliminarCarrera.as_view()), name='eliminar_carrera'),

    path('lista_asignatura/', login_required(ListaAsignatura.as_view()), name="listar_asignatura"),
    path('crea_asignatura/',login_required(CrearAsignatura.as_view()), name="crear_asignatura"),
    path('edita_asignatura/<int:pk>/', login_required(ActualizarAsignatura.as_view()), name='editar_asignatura'),
    path('elimina_asignatura/<int:pk>/', login_required(EliminarAsignatura.as_view()), name='eliminar_asignatura'),

    path('lista_docente/', login_required(ListaDocente.as_view()), name="listar_docente"),
    path('crea_docente/',login_required(CrearDocente.as_view()), name="crear_docente"),
    path('edita_docente/<int:pk>/', login_required(ActualizarDocente.as_view()), name='editar_docente'),
    path('elimina_docente/<int:pk>/', login_required(EliminarDocente.as_view()), name='eliminar_docente'),

    path('',include('app_istam.urls'))
]

admin.site.site_header = 'SISTEMA DE GESTION DE ESTUDIANTES'
