from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

class AppIstamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_istam'
