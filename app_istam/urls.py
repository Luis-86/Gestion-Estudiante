from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('', EstudianteViewset)
router.register('api/v1.0/matriculas', MatriculaViewset)
router.register('api/v1.0/asignaturas', AsignaturaViewset)
router.register('api/v1.0/docentes', DocenteViewset)
router.register('api/v1.0/carreras', CarreraViewset)
router.register('api/v1.0/perfiles', PerfilViewset)
urlpatterns = router.urls
