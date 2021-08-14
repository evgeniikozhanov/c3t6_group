import pytest

from c3t6_group.c3t6_group import C3T6Item


@pytest.mark.parametrize(
    "first_item,second_item,expected_result",
    [
        (C3T6Item('a', False), C3T6Item('a', False), False),
        (C3T6Item('a', False), C3T6Item('a', True), True),
        (C3T6Item('a', False), C3T6Item('b', True), False),
        (C3T6Item('b', True), C3T6Item('b', True), False),
        (C3T6Item('a', True), C3T6Item('b', True), False),
    ]
)
def test_check_cancellation_ability(c3t6_simple_group, first_item, second_item, expected_result):
    assert c3t6_simple_group.check_cancellation_ability(first_item, second_item) == expected_result
