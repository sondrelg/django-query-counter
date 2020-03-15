import logging
from functools import wraps
from typing import Callable

from django.core.exceptions import ImproperlyConfigured
from django.db import connection
from django.db.backends.base.base import BaseDatabaseWrapper

from django_qc.settings import settings

logger = logging.getLogger('django_qc')


def db_helper(count: int):
    """
    Decorator function to count DB queries.
    """
    # If the intended count of queries is higher than the max, connect.queries will reset.
    if count > BaseDatabaseWrapper.queries_limit:
        raise ImproperlyConfigured(f'Count cannot be higher than the max query limit of {BaseDatabaseWrapper.queries_limit}')

    def outer(fn: Callable):
        """
        Wrapper function - outer layer.
        """

        @wraps(fn)
        def inner(*args, **kwargs):
            query_count = len(connection.queries)
            fn(*args, **kwargs)
            actual_count = len(connection.queries) - query_count

            # If the amount of queries exceeds expectations
            if settings.DEBUG and actual_count != count:
                error_msg = f'Function `{fn.__name__}` performs {actual_count} queries, where we expected {count}'
                if settings.RAISE_EXC:
                    raise ImproperlyConfigured(error_msg)
                elif settings.LOG_EXC:
                    logger.exception(error_msg)
                else:
                    logger.warning(error_msg)

        return inner

    return outer
