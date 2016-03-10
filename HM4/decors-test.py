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

        self.assertEqual(wrapped(7), 42)
        self.assertEqual(func.call_count, 2)
