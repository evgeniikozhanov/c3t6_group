from c3t6_group.c3t6_group import C3T6Item


def test_simple_cancellation(c3t6_simple_group):
    res = c3t6_simple_group.do_simple_cancellation(
        (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False))
    )
    assert res == (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False)), str(res)
    res = c3t6_simple_group.do_simple_cancellation(
        (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False), C3T6Item('a', True))
    )
    assert res == (C3T6Item('c', False), C3T6Item('b', False)), str(res)
    res = c3t6_simple_group.do_simple_cancellation(
        (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('c', True), C3T6Item('a', False))
    )
    assert res == (C3T6Item('a', False), C3T6Item('a', False)), str(res)
