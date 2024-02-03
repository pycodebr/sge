from django.apps import AppConfig


class OutflowsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'outflows'

    def ready(self):
        import outflows.signals  # noqa: F401
