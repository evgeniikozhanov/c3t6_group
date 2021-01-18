from c3t6_group.c3t6_group import C3T6Group, C3T6Item


def test_c3t6_group():
    c3t6_group = C3T6Group(
        [
            C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False),
            C3T6Item('a', True), C3T6Item('b', True), C3T6Item('c', True)
        ],
        [
            (C3T6Item('a', False), C3T6Item('c', False), C3T6Item('b', False)),
            (C3T6Item('a', False), C3T6Item('b', False), C3T6Item('c', False))
        ]
    )

    assert c3t6_group.constitutive_relation == {
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
