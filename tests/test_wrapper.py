from inspect import getframeinfo, stack
from pathlib import Path
from random import randint

from tests.base import TestingBaseClass


def read_comment():
    """
    Returns the comment left by the wrapper function.
    """
    caller = getframeinfo(stack()[1][0])
    filename = str(Path(caller.filename).parent / 'base.py')
    with open(filename, 'r') as f:
        content = f.readlines()
    return content[19].replace('@db_helper()  #', '').replace('\n', '').strip()


class TestWrapper(TestingBaseClass):

    def test_incorrect_count(self):
        """
        Test that an n+1 error is caught and error is raised.
        """
        for _ in range(5):
            number = randint(0, 100)
            self.call(number)
            self.assertEqual(read_comment(), f'function ran {13 + number} queries')
