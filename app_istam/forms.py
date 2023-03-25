from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

class PerfilForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Ingrese el usuario'}
    ))

    telefono = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Ingrese el telefono'}
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Ingrese la contraseña'}
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Confirme la contraseña'}
    ))
 
    direccion = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Ingrese la direccion'}
    ))
    
    cedula = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control', 'placeholder':'Ingrese la cedula'}
    ))

    foto = forms.ImageField()

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombres','apellidos','cedula','correo', 'foto']
        labels = {
            'nombres': 'Nombre del Estudiante',
            'apellidos': 'Apellidos del Estudiante',
            'cedula':'Cedula del Estudiante',
            'correo':'Correo del Estudiante',
            'foto':'Foto del Estudiante',
        }
        widgets = {
            'nombres':(forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre','id':'nombres'},)),
            'apellidos':(forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el apellido','id':'apellidos'},)),
            'cedula':(forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre','id':'cedula'},)),
            'correo':(forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el correo','id':'correo'},)),
        }

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields =  ['num_matricula', 'fk_Estudiante', 'fk_Carrera', 'ciclo','fecha_matricula']
        labels = {
            'num_matricula': 'Numero de matricula',
            'fk_Estudiante': 'Datos del estudiante',
            'fk_Carrera':'Nombre de la carrera',
            'ciclo':'Curso del estudiante',
            'fecha_matricula':'Fecha de matricula',
        }
        widgets = {
            'num_matricula':(forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el numero de matricula','id':'num_matricula'},)),
            'fk_Estudiante':(forms.Select(attrs={'class':'form-control','placeholder':'Seleccione un estudiante','id':'fk_Estudiante'},)),
            'fk_Carrera':(forms.Select(attrs={'class':'form-control','placeholder':'Seleccione una carrera','id':'fk_Carrera'},)),
            'ciclo':(forms.Select(attrs={'class':'form-control','placeholder':'Seleccione el ciclo','id':'ciclo'},)),
            'fecha_matricula': (forms.DateInput(attrs={'class':'form-control fecha-picker','placeholder':'Ingrese la fecha','id':'fecha_matricula'},)),
        }

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields =  ['nombre', 'tipo_carrera']
        labels = {
            'nombre': 'Nombre de la carrrera',
            'tipo_carrera': 'Area a la que pertenece la carrera',
        }
        widgets = {
            'nombre':(forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre de la carrera','id':'nombre'},)),
            'tipo_carrera':(forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el tipo de carrera','id':'tipo_carrera'},)),   
        }

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombres','apellidos','cedula','correo']
        labels = {
            'nombres': 'Nombre del docente',
            'apellidos': 'Apellidos del docente',
            'cedula':'Cedula del docente',
            'correo':'Correo del docente',
        }
        widgets = {
            'nombres':(forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre','id':'nombres'},)),
            'apellidos':(forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el apellido','id':'apellidos'},)),
            'cedula':(forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese la cedula','id':'cedula'},)),
            'correo':(forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el correo','id':'correo'},)),
        }

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['codigo','nombres','creditos','docente']
        labels = {
            'codigo': 'Codigo de la asignatura',
            'nombres': 'Nombre de la asignatura',
            'creditos':'Creditos de la asignatura',
            'docente':'Docente de la asignatura',
        }
        widgets = {
            'codigo':(forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el codigo','id':'codigo'},)),
            'nombres':(forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre de la asignatura','id':'nombres'},)),
            'creditos':(forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese numero de creditos','id':'creditos'},)),
            'docente':(forms.Select(attrs={'class':'form-control','placeholder':'Seleccione un docente','id':'docente'},)),
        }