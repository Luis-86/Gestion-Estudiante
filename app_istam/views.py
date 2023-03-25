from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import *
from .models import *

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/inicio/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/lista_estudiante/')

        form = LoginForm()
        ctx = {'form': form}
        return render(request, 'login.html', ctx)


@login_required(login_url='/login/')
def inicio_view(request):
    estudiantes = Estudiante.objects.all()
    ctx = {'estudiantes': estudiantes}
    return render(request, 'index.html', ctx)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def registrar_view(request):
    info = "inicializar"
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            perfil = Perfil()
            perfil.usuario = user
            perfil.telefono = form.cleaned_data['telefono']
            perfil.direccion = form.cleaned_data['direccion']
            perfil.cedula = form.cleaned_data['cedula']
            perfil.foto = form.cleaned_data['foto']
            perfil.save()
            info = "GUARDADO SATISFACTORIAMENTE"
            ctx = {'info': info}
            return render(request, 'registro_exitoso.html', ctx)
    else:
        form = PerfilForm()
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None

    ctx = {'form': form}
    return render(request, 'registro_usuario.html', ctx)

#VISTAS BASADAS EN CLASE

#1 CLASE ESTUDIANTE
class ListaEstudiante(ListView):
    model = Estudiante
    template_name = 'dashboard/listar_estudiante.html'
    queryset = Estudiante.objects.filter(estado=True)
    context_object_name = 'estudiantes'

class CrearEstudiante(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'dashboard/crear_estudiante.html'
    success_url = reverse_lazy('listar_estudiante')

class ActualizarEstudiante(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'dashboard/editar_estudiante.html'
    success_url = reverse_lazy('listar_estudiante')

class EliminarEstudiante(DeleteView):
    model = Estudiante
    template_name = 'dashboard/estudiante_delete.html'
    def post(self, request, pk, *args, **kwargs):
        object = Estudiante.objects.get(id=pk)
        object.delete()
        return redirect('listar_estudiante')

#2 CLASE MATRICULA
class ListaMatricula(ListView):
    model = Matricula
    template_name = 'matricula/listar_matricula.html'
    queryset = Matricula.objects.all()
    context_object_name = 'matriculas'

class CrearMatricula(CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'matricula/crear_matricula.html'
    success_url = reverse_lazy('listar_matricula')

class ActualizarMatricula(UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'matricula/editar_matricula.html'
    success_url = reverse_lazy('listar_matricula')

class EliminarMatricula(DeleteView):
    model = Matricula
    template_name = 'matricula/matricula_delete.html'
    def post(self, request, pk, *args, **kwargs):
        object = Matricula.objects.get(id=pk)
        object.delete()
        return redirect('listar_matricula')

#3 CLASE CARRERA
class ListaCarrera(ListView):
    model = Carrera
    template_name = 'carrera/listar_carrera.html'
    queryset = Carrera.objects.all()
    context_object_name = 'carreras'

class CrearCarrera(CreateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'carrera/crear_carrera.html'
    success_url = reverse_lazy('listar_carrera')

class ActualizarCarrera(UpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'carrera/editar_carrera.html'
    success_url = reverse_lazy('listar_carrera')

class EliminarCarrera(DeleteView):
    model = Carrera
    template_name = 'carrera/carrera_delete.html'
    def post(self, request, pk, *args, **kwargs):
        object = Carrera.objects.get(id=pk)
        object.delete()
        return redirect('listar_carrera')

#4 CLASE DOCENTE
class ListaDocente(ListView):
    model = Docente
    template_name = 'docente/listar_docente.html'
    queryset = Docente.objects.all()
    context_object_name = 'docentes'

class CrearDocente(CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'docente/crear_docente.html'
    success_url = reverse_lazy('listar_docente')

class ActualizarDocente(UpdateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'docente/editar_docente.html'
    success_url = reverse_lazy('listar_docente')

class EliminarDocente(DeleteView):
    model = Docente
    template_name = 'docente/docente_delete.html'
    def post(self, request, pk, *args, **kwargs):
        object = Docente.objects.get(id=pk)
        object.delete()
        return redirect('listar_docente')
    
#5 CLASE ASIGNATURA
class ListaAsignatura(ListView):
    model = Asignatura
    template_name = 'asignatura/listar_asignatura.html'
    queryset = Asignatura.objects.all()
    context_object_name = 'asignaturas'

class CrearAsignatura(CreateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'asignatura/crear_asignatura.html'
    success_url = reverse_lazy('listar_asignatura')

class ActualizarAsignatura(UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'asignatura/editar_asignatura.html'
    success_url = reverse_lazy('listar_asignatura')

class EliminarAsignatura(DeleteView):
    model = Asignatura
    template_name = 'asignatura/asignatura_delete.html'
    def post(self, request, pk, *args, **kwargs):
        object = Asignatura.objects.get(id=pk)
        object.delete()
        return redirect('listar_asignatura')

