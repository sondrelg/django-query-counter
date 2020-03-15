#########################
Django Query Count Helper
#########################

.. image:: https://img.shields.io/pypi/v/django-qc.svg
    :target: https://pypi.org/project/django-qc/

.. image:: https://img.shields.io/pypi/pyversions/django-qc.svg
    :target: https://pypi.org/project/django-qc/

.. image:: https://img.shields.io/pypi/djversions/django-qc.svg
    :target: https://pypi.python.org/pypi/django-qc

.. image:: https://codecov.io/gh/sondrelg/django-query-counter/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sondrelg/django-query-counter

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://pypi.org/project/django-qc/

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit

This is a simple implementation of the `django_query_analyze` function detailed in
`The Django Speed Handbook: making a Django app faster <https://openfolder.sh/django-faster-
speed-tutorial?utm_campaign=Django%2BNewsletter&utm_medium=email&utm_source=Django_Newsletter_13>`_, featured in the
Django newsletter a few weeks back.

The idea is that you can wrap you pure db-query functions with a decorator, and make sure the function is calling the database as you expect it to.

.. code-block:: python

    from django_qc import db_helper
    from app.models import Song

    @db_helper(count=1)
    def get_songs():
        return serialize_songs(Song.objects.all(), many=True)

See the original article for a more thorough description of the issue.

Since the Django ORM is lazy, you will likely want to wrap your serializers rather than your queries, if they're not in the same function. For example:

.. code-block:: python

    from django_qc import db_helper

    @db_helper(count=1)
    def serialize_songs(song: Song)
        return {
            'name': song.name,
            'cd': song.cd.name,
        }

This package should only run during development.

************
Installation
************

Install using pip:

.. code-block:: bash

    pip install django-qc

********
Settings
********

There are three settings that can be configured:

.. code-block:: python

    DB_HELPER {
        'RAISE_EXC': True,
        'LOG_EXC': True,
        'DEBUG': DEBUG
    }


* :code:`RAISE_EXC`
        Whether or not to raise an error when the specified query count deviates the actual query count.

    Default: True

* :code:`LOG_EXC`
        Whether or not to log an exception (logger.exception) when the specified query count deviates the actual query count.
        If you're using Sentry or similar tools, an exception logger will raise an issue in the system.
        This only applies to when RAISE_EXC is False.

    Default: True

* :code:`DEBUG`
        Whether or not to check query counts at runtime.

    Default: True
