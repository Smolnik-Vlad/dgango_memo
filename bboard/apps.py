#в этом файле описывается ласс для работы с проектом
from django.apps import AppConfig


class BboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # вот здесь указывается то же самое, что и в settings
    name = 'bboard'

    def ready(self):
        from . import signals  # для активирования сигналов
