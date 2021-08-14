import unittest

from c3t6_group.c3t6_group import C3T6Group, C3T6Item


class C3T6GroupCommonTest(unittest.TestCase):

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

    def test_c3t6_group_constitutive_relation(self):

        assert self.c3t6_group.constitutive_relations == {
            (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False)),
            (C3T6Item('c', False), C3T6Item('b', False), C3T6Item('a', False)),
            (C3T6Item('b', False), C3T6Item('a', False), C3T6Item('c', False)),
            (C3T6Item('b', True), C3T6Item('c', True), C3T6Item('a', True)),
            (C3T6Item('a', True), C3T6Item('b', True), C3T6Item('c', True)),
            (C3T6Item('c', True), C3T6Item('a', True), C3T6Item('b', True)),

            (C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False)),
            (C3T6Item('b', False), C3T6Item('c', False), C3T6Item('a', False)),
            (C3T6Item('c', False), C3T6Item('a', False), C3T6Item('b', False)),
            (C3T6Item('c', True), C3T6Item('b', True), C3T6Item('a', True)),
            (C3T6Item('a', True), C3T6Item('c', True), C3T6Item('b', True)),
            (C3T6Item('b', True), C3T6Item('a', True), C3T6Item('c', True)),
        }

        for relation in self.c3t6_group.constitutive_relations:
            assert self.c3t6_group.do_simple_cancellation(relation) == relation
