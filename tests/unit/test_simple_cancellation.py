import unittest

from c3t6_group.c3t6_group import C3T6Group, C3T6Item


class TestSimpleCancellation(unittest.TestCase):

    def setUp(self) -> None:
        self.c3t6_group = C3T6Group(
            [
                C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False),
                C3T6Item('a', True), C3T6Item('b', True), C3T6Item('c', True)
            ],
            [
                (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False)),
                (C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False))
            ]
        )

    def test_simple_cancellation(self):
        res = self.c3t6_group.do_simple_cancellation(
            (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False))
        )
        assert res == (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False)), str(res)
        res = self.c3t6_group.do_simple_cancellation(
            (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False), C3T6Item('a', True))
        )
        assert res == (C3T6Item('c', False), C3T6Item('b', False)), str(res)
        res = self.c3t6_group.do_simple_cancellation(
            (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('c', True), C3T6Item('a', False))
        )
        assert res == (C3T6Item('a', False), C3T6Item('a', False)), str(res)
