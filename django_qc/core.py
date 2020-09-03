import logging
from functools import wraps
from inspect import getframeinfo, stack
from typing import Callable, Dict

from django.db import connections

logger = logging.getLogger('django_qc')


def db_helper(verbose=False):
    """
    Decorator function to count DB queries.
    """
    caller = getframeinfo(stack()[1][0])
    wrapper_line_number = caller.lineno - 1

    def write_line_comment(pre_call_query_counts: Dict[str, int], post_call_query_counts: Dict[str, int]) -> str:
        """
        Writes a comment to the end of the line above the function definition.
        """
        # Read original content
        with open(caller.filename, 'r') as f:
            content = f.readlines()

        # Get the original line, minus any existing comments and newlines
        original_line = content[wrapper_line_number].split("  #")[0].replace("\n", "")

        # Sum up the total amount of queries made during the function call
        pre_sum = sum(value for value in post_call_query_counts.values())
        post_sum = sum(value for value in pre_call_query_counts.values())

        # Create comments
        comment = f'function ran {pre_sum - post_sum} queries'
        if verbose:
            query_sum_per_database_handler = {
                k: (new - original)
                for (k, original), (_, new)
                in zip(pre_call_query_counts.items(), post_call_query_counts.items())
            }
            comment += f' - details: {str(query_sum_per_database_handler)}'

        content[wrapper_line_number] = f'{original_line}  # {comment}\n'

        with open(caller.filename, 'w') as f:
            f.write(''.join(content))

        return comment

    def outer(fn: Callable):
        """
        Wrapper function - outer layer.
        """

        @wraps(fn)
        def inner(*args, **kwargs):
            pre_call_query_counts = {k: len(connections[k].queries) for k in connections._databases.keys()}
            output = fn(*args, **kwargs)
            post_call_query_counts = {k: len(connections[k].queries) for k in connections._databases.keys()}
            comment = write_line_comment(pre_call_query_counts, post_call_query_counts)
            logger.info('Added comment `%s` above function %s', comment, fn.__name__)
            return output

        return inner

    return outer
