from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

def url(self, filename):
    ruta = "static/img/estudiantes/%s/%s" % (self.nombres, str(filename))
    return ruta

class Estudiante(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10, unique=True)
    correo = models.EmailField()
    foto = models.ImageField(upload_to=url, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombres
    
    def foto_estudiante(self):
        return mark_safe('<a href="/%s" target="_blank"> <img src="/%s" width="60px" height="70px"> </a>' % (self.foto, self.foto))
    foto_estudiante.allow_tags = True
    
    
tipo_pro = [
    ('001', 'TECNOLOGICA'),
    ('002', 'ADMINISTRACION'),
]
    
class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_carrera = models.CharField(max_length=45, choices=tipo_pro)

  
    def __str__(self):
        return self.nombre
tipo_ciclo = [
    ('1', 'I CICLO'),
    ('2', 'II CICLO'),
    ('3', 'III CICLO'),
    ('4', 'IV CICLO'),
    ('5', 'V CICLO'),
]

class Matricula(models.Model):
    num_matricula = models.IntegerField()
    fk_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fk_Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    ciclo = models.CharField(max_length=10, choices=tipo_ciclo, default='available')
    fecha_matricula = models.DateField()
 
    def __str__(self):
        return self.periodo_academico
    
class Docente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return self.nombres
    

class Asignatura(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=100)
    creditos = models.PositiveSmallIntegerField()
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres
    
def url_perfil(self, filename):
    ruta = "static/img/perfiles/%s/%s" % (self.usuario, str(filename))
    return ruta


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    direccion = models.TextField()
    cedula = models.CharField(max_length=10)
    foto = models.ImageField(upload_to=url_perfil)

    def foto_perfil(self):
        return mark_safe('<a href="/%s" target="_blank"> <img src="/%s" width="60px" height="70px"> </a>' % (self.foto, self.foto))
    foto_perfil.allow_tags = True
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
 


