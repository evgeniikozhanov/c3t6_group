from dataclasses import dataclass
from typing import Tuple, Iterable


@dataclass
class C3T6Item:
    value: str
    is_reversed: bool

    @classmethod
    def create_from_another_instance(cls, c3t6_item: 'C3T6Item', force_reversed=False):
        return cls(value=c3t6_item.value, is_reversed=(force_reversed or c3t6_item.is_reversed))

    def __hash__(self):
        return hash(f'{"-" if self.is_reversed else ""}{self.value}')


class C3T6Group:
    def __init__(self, forming_alphabet: Iterable[C3T6Item], constitutive_relation: Iterable[Tuple[C3T6Item]]):
        self.forming_alphabet = set(forming_alphabet)
        self.constitutive_relation = \
            self.get_all_inverse_relations(self.get_all_permutations(set(constitutive_relation)))

    @staticmethod
    def get_all_permutations(constitutive_relation_init):
        constitutive_relation_new = set()
        for cr in constitutive_relation_init:
            for i in range(1, len(cr)):
                constitutive_relation_new.add(
                    tuple([C3T6Item.create_from_another_instance(j) for j in cr[i:]] +
                          [C3T6Item.create_from_another_instance(k) for k in cr[:i]]))
        return constitutive_relation_new.union(constitutive_relation_init)

    @staticmethod
    def get_all_inverse_relations(constitutive_relation_init):
        constitutive_relation_new = set()
        for cr in constitutive_relation_init:
            constitutive_relation_new.add(
                tuple([C3T6Item.create_from_another_instance(j, force_reversed=(not j.is_reversed)) for j in cr[::-1]]))
        return constitutive_relation_new.union(constitutive_relation_init)
