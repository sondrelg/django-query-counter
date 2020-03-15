from django.conf import settings
from django.test import TestCase

from django_qc.core import db_helper
from tests.models import CD, Song


class TestingBaseClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        cd = CD.objects.create(name='myAlbum')
        for i in range(12):
            Song.objects.create(name=f'song-{i}', cd=cd)

    def setUp(self) -> None:
        settings.DEBUG = True

    def call(self, count):
        @db_helper(count=count)
        def call_db():
            songs = Song.objects.all()
            for song in songs:
                _ = (song.name, song.cd)

        call_db()
