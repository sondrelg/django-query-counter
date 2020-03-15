import sys

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class Settings(object):
    """
    Reads and validates django_qc settings.
    """

    def __init__(self):
        self.RAISE_EXC = True
        self.LOG_EXC = True
        self.DEBUG = True

        if hasattr(settings, 'DB_HELPER'):
            db_helper_settings = settings.DB_HELPER
            for setting, value in db_helper_settings.items():
                if hasattr(self, setting):
                    setattr(self, setting, value)
                else:
                    raise ImproperlyConfigured(f'`{setting}` is not a valid setting for DB_HELPER')

        if self.DEBUG and not settings.DEBUG and 'test' not in sys.argv:
            raise ImproperlyConfigured('DB-helper should only run when DEBUG is True')


settings = Settings()
