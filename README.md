![https://pypi.org/project/django-qc/](https://img.shields.io/pypi/v/django-qc.svg)
![https://pypi.org/project/django-qc/](https://img.shields.io/pypi/pyversions/django-qc.svg)
![https://pypi.python.org/pypi/django-qc](https://img.shields.io/pypi/djversions/django-qc.svg)
![https://codecov.io/gh/sondrelg/django-query-counter](https://codecov.io/gh/sondrelg/django-query-counter/branch/master/graph/badge.svg)
![https://pypi.org/project/django-qc/](https://img.shields.io/badge/code%20style-black-000000.svg)
![https://github.com/pre-commit/pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

## Django query counter - simple query debugging

Lets you easily catch and fix database query inefficiencies during development by decorating any function or method.

![Query counter](https://raw.githubusercontent.com/sondrelg/django-query-counter/master/docs/comments.gif)

The main potential drawback of seeing query data in your code is that commits can become cluttered. We therefore recommend pairing django-qc with a [pre-commit hook for removing the comments](https://github.com/sondrelg/remove-query-counts) before they are ever even committed.

## Installation

Install using pip:

    pip install django-qc

## Usage

Simply import the db_helper wrapper and pass `verbose=True` if you want more details than in the default setting.

```python
from django_qc import db_helper

@db_helper(verbose=True)
def my_function():
    ...
```

## Settings

There's only one setting to configure, but it is required:

```python
DB_HELPER {
    'DEBUG': DEBUG
}
```

Decorator functions will not do anything if debug is `False`, and by design does not allow a debug value of `True` if the general Django debug value is `False`, as this is intended as a development aid only.
