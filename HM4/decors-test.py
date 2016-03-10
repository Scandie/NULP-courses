from mock import Mock
from decorators import memo
from unittest import TestCase


class DecoratorsTestCase(TestCase):

    def test_wrap_memo(self):

        func = Mock(name='func')
        func.return_value = 42

        wrapped = memo(func)
        # First call gives a call count of 1
        self.assertEqual(wrapped(3), 42)
        self.assertEqual(func.call_count, 1)

        self.assertEqual(wrapped(3), 42)
        self.assertEqual(func.call_count, 1)

        self.assertEqual(wrapped(x=7, y=1, z=2), 42)
        self.assertEqual(func.call_count, 2)

        self.assertEqual(wrapped(y=1, x=7, z=2), 42)
        self.assertEqual(func.call_count, 2)

        self.assertEqual(wrapped(7, 1, 2), 42)     # doesn't matter, is is args or kwargs one call of function
        self.assertEqual(func.call_count, 2)       # arguments in cache should be the same

        self.assertEqual(wrapped(7, 2, 2), 42)
        self.assertEqual(func.call_count, 3)

        self.assertEqual(wrapped([7]), 42)
        self.assertEqual(func.call_count, 4)

        self.assertEqual(wrapped([7]), 42)         # cause list isn't hashable
        self.assertEqual(func.call_count, 5)
