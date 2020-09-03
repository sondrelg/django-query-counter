![https://pypi.org/project/django-qc/](https://img.shields.io/pypi/v/django-qc.svg)
![https://pypi.org/project/django-qc/](https://img.shields.io/pypi/pyversions/django-qc.svg)
![https://pypi.python.org/pypi/django-qc](https://img.shields.io/pypi/djversions/django-qc.svg)
![https://codecov.io/gh/sondrelg/django-query-counter](https://codecov.io/gh/sondrelg/django-query-counter/branch/master/graph/badge.svg)
![https://pypi.org/project/django-qc/](https://img.shields.io/badge/code%20style-black-000000.svg)
![https://github.com/pre-commit/pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

## Django query counter - simple query debugging

Lets you easily catch and fix database query inefficiencies during development by decorating any function or method.

![Query counter](https://raw.githubusercontent.com/sondrelg/django-query-counter/master/docs/comments.gif)

The only real drawback of getting updated query numbers in your code seems to be that it might receive a lot of attention during code reviews, so we recommend pairing it with a [pre-commit hook for removing the comments](https://github.com/sondrelg/remove-query-counts) before they are committed. If you're not familiar with [pre-commit](https://pre-commit.com/) it might be worth five minutes of your time to read up on.

## Installation

Install using pip:

    pip install django-qc

## Settings

There's only one setting to configure, but it is required:

```python
DB_HELPER {
    'DEBUG': DEBUG
}
```

Decorator functions will not do anything if debug is `False`, and by design does not allow a debug value of `True` if the general Django debug value is `False`, as this is intended as a development aid only.
