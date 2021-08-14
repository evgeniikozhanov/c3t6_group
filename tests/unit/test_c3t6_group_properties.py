from c3t6_group.c3t6_group import C3T6Item


def test_c3t6_group_constitutive_relation(c3t6_simple_group):
    """
    Does it guarantee that C(3) is satisfied?
    """

    assert c3t6_simple_group.constitutive_relations == {
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

    for relation in c3t6_simple_group.constitutive_relations:
        assert c3t6_simple_group.do_simple_cancellation(relation) == relation
