import pytest

from c3t6_group.c3t6_group import C3T6Item, C3T6Group
from c3t6_group.exceptions import T6ConditionViolated
from c3t6_group.utils import check_t6_group_property, look_for_inversed_elements


@pytest.mark.parametrize(
    "word_item,expected_result",
    [
        ((C3T6Item('a', False), C3T6Item('c', False), C3T6Item('a', True)), True),
        ((C3T6Item('a', False), C3T6Item('a', True), C3T6Item('b', True)), True),
        ((C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False)), False),
        ((C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', True)), False),
        ((C3T6Item('a', False), C3T6Item('b', True), C3T6Item('c', True)), False),
    ]
)
def test_look_for_inversed_elements(word_item, expected_result):
    assert look_for_inversed_elements(word_item) == expected_result


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
def test_checking_t6_group_property_successful(group_item):
    assert check_t6_group_property(group_item)


@pytest.mark.parametrize(
    "group_item",
    [
        C3T6Group(
            [
                C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False),
                C3T6Item('a', True), C3T6Item('b', True), C3T6Item('c', True)
            ],
            [
                (C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False), C3T6Item('c', False)),
            ]
        ),
    ]
)
def test_checking_t6_group_property_failure(group_item):
    with pytest.raises(T6ConditionViolated):
        check_t6_group_property(group_item)
