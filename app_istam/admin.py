from django.contrib import admin
from .models import *
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin

# class EstudianteResource(resources.ModelResource):
#     class Meta:
#         model = Estudiante
#         model = Carrera
#         model = Matricula
#         model = Docente
#         model = Asignatura

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'correo', 'foto_estudiante','estado')
    search_fields = ['nombres', 'apellidos']
    # resources_class = EstudianteResource

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('num_matricula', 'fk_Estudiante', 'fk_Carrera', 'ciclo','fecha_matricula')
    search_fields = ['nombre', 'tipo_carrera']

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_carrera')
    search_fields = ['nombre', 'tipo_carrera']

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'correo')
    search_fields = ['nombres', 'apellidos']

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombres', 'creditos', 'docente')
    search_fields = ['nombres', 'creditos', 'docente']

class PerfilAdmin(admin.ModelAdmin):
    list_display=('cedula','usuario','telefono','direccion','foto_perfil')
    search_fields=['cedula','usuario']

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Matricula, MatriculaAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Perfil, PerfilAdmin)
