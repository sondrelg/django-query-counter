from unittest.mock import patch

from django.core.exceptions import ImproperlyConfigured

from django_qc.core import db_helper
from tests.base import TestingBaseClass
from tests.models import Song


class TestWrapper(TestingBaseClass):

    def test_incorrect_count(self):
        """
        Test that an n+1 error is caught and error is raised.
        """
        with self.assertRaisesRegexp(ImproperlyConfigured, '`call_db` performed 13 queries, where we expected 1'):
            self.call(1)

    @patch('django_qc.core.settings.RAISE_EXC', False)
    def test_correct_error_logging(self):
        """
        An exception logger should be logged if RAISE_EXC is False.
        """
        with self.assertLogs(level='ERROR') as log:
            self.call(1)
            self.assertIn('Function `call_db` performed 13 queries, where we expected 1', log.output[0])

    @patch('django_qc.core.settings.RAISE_EXC', False)
    @patch('django_qc.core.settings.LOG_EXC', False)
    def test_warning_logging(self):
        """
        One warning logger should be raised if both settings are False.
        """
        with self.assertLogs(level='WARNING') as log:
            self.call(1)
            self.assertIn('Function `call_db` performed 13 queries, where we expected 1', log.output[0])
            self.assertEqual(1, len(log.output))  # If more than 1, logging is incorrectly set up

    def test_exceeded_maximum_count(self):
        """
        Verify that an error is raised if count exceeds the max.
        """
        with self.assertRaisesRegexp(ImproperlyConfigured, 'Count cannot be higher than the max query limit of 9000'):
            @db_helper(count=9001)
            def _():
                pass

    def test_correct_count(self):
        """
        Good DB call.
        """
        @db_helper(count=1)
        def call_db_well():
            songs = Song.objects.all().prefetch_related('cd')
            for song in songs:
                _ = (song.name, song.cd)
