from dataclasses import dataclass
from typing import Tuple, Iterable, List, Set


@dataclass
class C3T6Item:
    value: str
    is_reversed: bool

    @classmethod
    def create_from_another_instance(cls, c3t6_item: 'C3T6Item', force_reversed=False) -> 'C3T6Item':
        """
        This method make an inverse or copy item of concrete C3T6Item. This helps us to get an inverse of the word.
        Also this helps us to get a permutation of the word.
        """
        return cls(value=c3t6_item.value, is_reversed=(force_reversed or c3t6_item.is_reversed))

    def __hash__(self):
        return hash(str())

    def __str__(self):
        return f'{"-" if self.is_reversed else ""}{self.value}'


class C3T6Group:
    """
    group_alphabet - set of all C3-T6 items, which can use to create words
    constitutive_relations - relations that define words equals 1 (an empty string in our case)
    """

    def __init__(self, group_alphabet: Iterable[C3T6Item], constitutive_relations: Iterable[Tuple[C3T6Item, ...]]):
        self.group_alphabet: set = set(group_alphabet)
        self.constitutive_relations: set = \
            self.get_all_inverse_relations(self.get_all_permutations(set(constitutive_relations)))

    @staticmethod
    def get_new_permutation(
            constitutive_relation: Tuple[C3T6Item, ...], permutation_start_position: int
    ) -> Tuple[C3T6Item, ...]:
        """
        Return permutation of the word

        For example, for word abcde and start position 2 it returns cdeab (cde + ab)
        """
        return tuple(
            [C3T6Item.create_from_another_instance(j) for j in constitutive_relation[permutation_start_position:]] +
            [C3T6Item.create_from_another_instance(k) for k in constitutive_relation[:permutation_start_position]]
        )

    def get_all_permutations(self, constitutive_relations_init: Set[Tuple[C3T6Item, ...]]) -> Set[Tuple[C3T6Item, ...]]:
        """ Return  """
        constitutive_relations_new = set()
        for cr in constitutive_relations_init:
            for i in range(1, len(cr)):
                constitutive_relations_new.add(
                    self.get_new_permutation(cr, i)
                )
        return constitutive_relations_new.union(constitutive_relations_init)

    @staticmethod
    def get_all_inverse_relations(constitutive_relations_init):
        """  """
        constitutive_relations_new = set()
        for cr in constitutive_relations_init:
            constitutive_relations_new.add(
                tuple([C3T6Item.create_from_another_instance(j, force_reversed=(not j.is_reversed)) for j in cr[::-1]]))
        return constitutive_relations_new.union(constitutive_relations_init)

    def do_simple_cancellation(self, word: Tuple[C3T6Item, ...]):
        """  """
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
