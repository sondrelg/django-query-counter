import sys
from unittest.mock import patch

from django.core.exceptions import ImproperlyConfigured
from django.test import SimpleTestCase

from django_qc.settings import Settings


class TestSettings(SimpleTestCase):
    """
    Tests package settings.
    """

    @patch('django_qc.settings.django_settings')
    def test_excess_input(self, setting):
        """
        Make sure we alert the user about excess settings, as this is most likely a mistake on their part.
        """
        setting.DB_HELPER = {'TEST': 'test'}
        with self.assertRaisesRegexp(ImproperlyConfigured, '`TEST` is not a valid setting for DB_HELPER'):
            Settings()

    @patch('django_qc.settings.django_settings')
    def test_debug_false(self, setting):
        """
        Make sure we alert the user when trying to run the program if DEBUG is false.
        """
        setting.DEBUG = False
        if 'test' in sys.argv:
            sys.argv.pop(sys.argv.index('test'))
        with self.assertRaisesRegexp(ImproperlyConfigured, 'DB-helper should only run when DEBUG is True'):
            Settings()
