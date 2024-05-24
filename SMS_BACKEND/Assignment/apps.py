from django.apps import AppConfig


class AssignmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Assignment'
    def ready(self) -> None:
        from . import signals