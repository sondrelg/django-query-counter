![https://pypi.org/project/django-qc/](https://img.shields.io/pypi/v/django-qc.svg)

![https://pypi.org/project/django-qc/](https://img.shields.io/pypi/pyversions/django-qc.svg)

![https://pypi.python.org/pypi/django-qc](https://img.shields.io/pypi/djversions/django-qc.svg)

![https://codecov.io/gh/sondrelg/django-query-counter](https://codecov.io/gh/sondrelg/django-query-counter/branch/master/graph/badge.svg)

![https://pypi.org/project/django-qc/](https://img.shields.io/badge/code%20style-black-000000.svg)

![https://github.com/pre-commit/pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

## Django Query Counter - Simple query monitoring

Django query counter lets you quickly identify ineffective selectors by showing you the number of queries made to the database.

Because the database query log can be a bit fickle, we've found that it's very convenient to simply show the number of queries made in the code.


The idea is that you can wrap you pure db-query functions with a decorator, and make sure the function is calling the database as you expect it to.

```python
    from django_qc import db_helper
    from app.models import Song

    @db_helper(count=1)
    def get_songs():
        return serialize_songs(Song.objects.all(), many=True)

```


See the original article for a more thorough description of the issue.

Since the Django ORM is lazy, you will likely want to wrap your serializers rather than your queries, if they're not in the same function. For example:

```python
    from django_qc import db_helper

    @db_helper(count=1)
    def serialize_songs(song: Song)
        return {
            'name': song.name,
            'cd': song.cd.name,
        }

```

This package should only run during development.


## Installation

Install using pip:

    pip install django-qc

## Settings

There are three settings that can be configured:

```python
    DB_HELPER {
        'DEBUG': DEBUG
    }
```


    `DEBUG`
        Whether or not to check query counts at runtime.

    Default: True
