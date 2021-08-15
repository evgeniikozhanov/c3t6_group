from itertools import combinations, islice, chain
from typing import Iterable, Tuple

from c3t6_group.c3t6_group import C3T6Group, C3T6Item
from c3t6_group.exceptions import C3ConditionViolated, T6ConditionViolated


def check_c3_group_property(c3t6_group: C3T6Group, p: int = 3):
    """
    There is no defining relator can be written as a reduced product of fewer than p pieces.
    """
    for r in c3t6_group.constitutive_relations:
        if len(c3t6_group.do_simple_cancellation(r)) < p:
            raise C3ConditionViolated
    return True


def look_for_inversed_elements(chain_for_checking: Iterable[C3T6Item]) -> bool:
    for item, next_item in zip(
            chain_for_checking,
            chain(islice(chain_for_checking, 1, None), islice(chain_for_checking, 0, 1))
    ):
        if item.value == next_item.value and item.is_reversed != next_item.is_reversed:
            return True
    return False


def check_simple_cancellation(c3t6_group: C3T6Group, word_for_checking: Tuple[C3T6Item]):
    return len(c3t6_group.do_simple_cancellation(word_for_checking)) == len(word_for_checking)


def check_t6_group_property(c3t6_group: C3T6Group, q: int = 6):
    for i in range(3, q):
        for chain_to_check in combinations(c3t6_group.constitutive_relations, i):
            for item, next_item in zip(
                    chain_to_check,
                    chain(islice(chain_to_check, 1, None), islice(chain_to_check, 0, 1))
            ):
                if look_for_inversed_elements(tuple(item) + tuple(next_item)):
                    continue

            for item, next_item in zip(
                    chain_to_check,
                    chain(islice(chain_to_check, 1, None), islice(chain_to_check, 0, 1))
            ):
                if check_simple_cancellation(c3t6_group, tuple(item) + tuple(next_item)):
                    break
            else:  # at least one of the products r1r2,...,rt−1rt, rtr1 is freely reduced as written
                raise T6ConditionViolated
    return True
