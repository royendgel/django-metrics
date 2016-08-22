from time import sleep

from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'app_metrics'

    def ready(self):
        pass
