![https://pypi.org/project/django-qc/](https://img.shields.io/pypi/v/django-qc.svg)
![https://pypi.org/project/django-qc/](https://img.shields.io/pypi/pyversions/django-qc.svg)
![https://pypi.python.org/pypi/django-qc](https://img.shields.io/pypi/djversions/django-qc.svg)

![https://codecov.io/gh/sondrelg/django-query-counter](https://codecov.io/gh/sondrelg/django-query-counter/branch/master/graph/badge.svg)
![https://pypi.org/project/django-qc/](https://img.shields.io/badge/code%20style-black-000000.svg)
![https://github.com/pre-commit/pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

## Django Query Counter - simple query debugging

Lets you easily catch and fix database query inefficiencies during development.

![Query counter](https://raw.githubusercontent.com/sondrelg/django-query-counter/master/docs/comment.gif)

Best paired with a [pre-commit hook for removing comments](https://github.com/sondrelg/remove-query-counts) before them to version control.

## Installation

Install using pip:

    pip install django-qc

## Settings

There's only one setting to configure:

```python
DB_HELPER {
    'DEBUG': DEBUG
}
```

The package will turn off if debug is False, and will not run if the Django debug setting is False, as this is not a product intended to run in production environments.
