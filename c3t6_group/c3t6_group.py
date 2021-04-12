from dataclasses import dataclass
from typing import Tuple, Iterable, List


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
    def __init__(self, forming_alphabet: Iterable[C3T6Item], constitutive_relation: Iterable[Tuple[C3T6Item, ...]]):
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

    def do_simple_cancellation(self, word: Tuple[C3T6Item, ...]):
        new_word: List[C3T6Item] = list(word)
        for i in range(len(word)):
            if word[i].value == word[i - 1].value and word[i].is_reversed != word[i - 1].is_reversed:
                if i == 0:
                    new_word = new_word[1:-1]
                else:
                    new_word = new_word[:i - 1] + new_word[i + 1:]
                break
        else:
            return word
        return self.do_simple_cancellation(tuple(new_word))
