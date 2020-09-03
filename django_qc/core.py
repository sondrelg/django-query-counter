import logging
from functools import wraps
from inspect import getframeinfo, stack
from typing import Callable, Dict

from django.db import connections

from django_qc.settings import settings

logger = logging.getLogger('django_qc')


def db_helper(verbose: bool = False):
    """
    Decorator function to count DB queries.
    """
    caller = getframeinfo(stack()[1][0])
    wrapper_line_number = caller.lineno - 1

    def write_line_comment(pre_call_query_counts: Dict[str, int], post_call_query_counts: Dict[str, int], function_name: str) -> None:
        """
        Writes a comment to the end of the line above the function definition.
        """
        # Read original content
        try:
            with open(caller.filename, 'r') as f:
                content = f.readlines()
        except OSError as e:
            # When executing commands in terminal, caller.filename becomes <input>
            logger.debug('Failed reading filepath. Error: %s', e)
            return

        # Get the original line, minus any existing comments and newlines
        original_comment = ''
        try:
            if len(content[wrapper_line_number].split('  # ')) != 0:
                original_comment = content[wrapper_line_number].split('  # ')[1].replace('\n', '').strip()
        except Exception as e:
            logger.debug('Failed setting original comment. Error: %s', e)

        original_line = content[wrapper_line_number].split('  #')[0].replace('\n', '')

        # Sum up the total amount of queries made during the function call
        pre_sum = sum(value for value in post_call_query_counts.values())
        post_sum = sum(value for value in pre_call_query_counts.values())

        # Create comments
        comment = f'function ran {pre_sum - post_sum} {"queries" if pre_sum - post_sum != 1 else "query"}'
        if verbose:
            query_sum_per_database_handler = {
                k: (new - original)
                for (k, original), (_, new)
                in zip(pre_call_query_counts.items(), post_call_query_counts.items())
            }
            comment += f' - details: {str(query_sum_per_database_handler)}'

        if comment.strip() != original_comment.strip():
            content[wrapper_line_number] = f'{original_line}  # {comment}\n'
            with open(caller.filename, 'w') as f:
                f.write(''.join(content))
            logger.info('Added comment `%s` above function %s', comment, function_name)
        else:
            logger.debug('Comment already exists for function %s', function_name)

    def outer(fn: Callable):
        """
        Wrapper function - outer layer.
        """

        @wraps(fn)
        def inner(*args, **kwargs):
            if settings.DEBUG:
                pre_call_query_counts = {k: len(connections[k].queries) for k in connections._databases.keys()}
                output = fn(*args, **kwargs)
                post_call_query_counts = {k: len(connections[k].queries) for k in connections._databases.keys()}
                write_line_comment(pre_call_query_counts, post_call_query_counts, fn.__name__)
                return output
            else:
                return fn(*args, **kwargs)

        return inner

    return outer
