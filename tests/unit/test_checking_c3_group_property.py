import pytest

from c3t6_group.c3t6_group import C3T6Item, C3T6Group
from c3t6_group.exceptions import C3ConditionViolated
from c3t6_group.utils import check_c3_group_property


@pytest.mark.parametrize(
    "group_item",
    [
        C3T6Group(
            [
                C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False),
                C3T6Item('a', True), C3T6Item('b', True), C3T6Item('c', True)
            ],
            [
                (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False)),
                (C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False))
            ]
        ),
    ]
)
def test_checking_c3_group_property_successful(group_item):
    assert check_c3_group_property(group_item)


@pytest.mark.parametrize(
    "group_item",
    [
        C3T6Group(
            [
                C3T6Item('a', False), C3T6Item('b', False),
                C3T6Item('a', True), C3T6Item('b', True),
            ],
            [
                (C3T6Item('a', False), C3T6Item('b', False), C3T6Item('b', True)),
                (C3T6Item('a', False), C3T6Item('a', False), C3T6Item('b', True))
            ]
        ),
    ]
)
def test_checking_c3_group_property_failure(group_item):
    with pytest.raises(C3ConditionViolated):
        check_c3_group_property(group_item)
