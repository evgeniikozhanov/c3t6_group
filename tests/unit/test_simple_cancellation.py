import pytest

from c3t6_group.c3t6_group import C3T6Item


@pytest.mark.parametrize(
    "word_to_cancel,expected_result",
    [
        (
                (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False)),
                (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False)),
        ),
        (
                (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False), C3T6Item('a', True)),
                (C3T6Item('c', False), C3T6Item('b', False)),
        ),
        (
                (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('c', True), C3T6Item('a', False)),
                (C3T6Item('a', False), C3T6Item('a', False)),
        ),
    ]
)
def test_simple_cancellation(c3t6_simple_group, word_to_cancel, expected_result):
    assert c3t6_simple_group.do_simple_cancellation(word_to_cancel) == expected_result
