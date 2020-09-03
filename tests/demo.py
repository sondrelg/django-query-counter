from django_qc import db_helper
from tests.models import CD


@db_helper()
def simple_query():
    cds = CD.objects.all()
    _ = cds.count()
    return cds


@db_helper()
def n_plus_one():
    _ = [cd.song.all().count() for cd in simple_query()]


@db_helper()
def prefetched_query():
    cds = CD.objects.all()
    _ = cds.count()
    return cds


@db_helper()
def just_one():
    _ = [cd.song.all().count() for cd in simple_query()]

just_one()
