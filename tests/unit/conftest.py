import pytest

from c3t6_group.c3t6_group import C3T6Group, C3T6Item


@pytest.fixture()
def c3t6_simple_group():
    return C3T6Group(
        [
            C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False),
            C3T6Item('a', True), C3T6Item('b', True), C3T6Item('c', True)
        ],
        [
            (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False)),
            (C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False))
        ]
    )
