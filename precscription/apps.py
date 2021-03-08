from django.apps import AppConfig


class PrecscriptionConfig(AppConfig):
    """
    Use to connect signals.
    """
    name = 'precscription'

    def ready(self):
        import precscription.signals

