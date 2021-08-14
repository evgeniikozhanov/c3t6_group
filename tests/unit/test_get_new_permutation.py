import pytest

from c3t6_group.c3t6_group import C3T6Item


@pytest.mark.parametrize(
    "constitutive_relation,permutation_start_position,expected_result",
    [
        (
                tuple([C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False)]),
                1,
                tuple([C3T6Item('b', False), C3T6Item('c', False), C3T6Item('a', False)])
        ),
        (
                tuple([C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False)]),
                2,
                tuple([C3T6Item('c', False), C3T6Item('a', False), C3T6Item('b', False)])
        ),
    ]
)
def test_get_new_permutation(constitutive_relation, permutation_start_position, expected_result, c3t6_simple_group):
    assert c3t6_simple_group.get_new_permutation(
        constitutive_relation=constitutive_relation,
        permutation_start_position=permutation_start_position
    ) == expected_result
