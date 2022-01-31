
import functools
from pprint import pprint

from dataclasses import dataclass
from collections import defaultdict
from typing import Dict, Optional, Callable, List


hprint = functools.partial(print, "\n#")


@dataclass
class Data:
    name: str
    x: int
    y: int


class HashMap:

    def __init__(
        self,
        hash_function: Callable[[str], int]
    ) -> None:
        self._table: Dict[int, List[Data]] = defaultdict(list)
        self._hash_function = functools.lru_cache(hash_function)

    def contains(self, name: str) -> bool:
        hash_index = self._hash_function(name)

        data_items = self._table[hash_index]

        filtered_items = list(
            filter(lambda item: item.name == name, data_items)
        )

        if len(filtered_items) == 1:
            return True

        return False

    def get(self, name: str) -> Optional[Data]:
        hash_index = self._hash_function(name)
        data_items = self._table.get(hash_index)

        if data_items is None:
            return None

        try:
            return list(filter(lambda item: item.name == name, data_items))[0]
        except IndexError:
            return None

    def insert(self, data: Data) -> bool:
        if self.contains(data.name):
            return False

        hash_index = self._hash_function(data.name)
        self._table[hash_index].append(data)

        return True

    def remove(self, name: str) -> Optional[Data]:
        if not self.contains(name):
            return None

        hash_index = self._hash_function(name)
        data_items = self._table[hash_index]

        target = list(filter(lambda item: item.name == name, data_items))[0]

        self._table[hash_index].remove(target)

        return target


def hash_f1(characters: str) -> int:
    hash_index = 0

    for c in characters:
        hash_index += ord(c)

    return hash_index


def main() -> None:
    hash_map_1 = HashMap(hash_f1)
    hash_map_2 = HashMap(hash)  # use Python's strong hash function

    hprint("Generate some data")
    d1 = Data("abc", 7, 9)
    d2 = Data("nA", 11, 22)
    d3 = Data("mB", 33, 44)
    print(d1)
    print(d2)
    print(d3)

    hprint("Insert #1")
    print(d1)
    print(d2)
    hash_map_1.insert(d1)
    hash_map_2.insert(d1)
    hash_map_1.insert(d2)
    hash_map_2.insert(d2)

    hprint("Table")
    pprint(hash_map_1._table)
    pprint(hash_map_2._table)

    hprint("Get the ones from #1")
    x = hash_map_1.get(d1.name)
    print("HM1", x)
    x = hash_map_2.get(d1.name)
    print("HM2", x)

    x = hash_map_1.get(d2.name)
    print("HM1", x)
    x = hash_map_2.get(d2.name)
    print("HM2", x)

    hprint("Check if d3 is in")
    k = hash_map_1.contains(d3.name)
    print("HM1", k)

    k = hash_map_2.contains(d3.name)
    print("HM2", k)
    print("if it's true, then it is obvious that there is a hashing conflict")

    hprint("Insert a conflicting node")
    print(d3)

    res = hash_map_1.insert(d3)
    print("Inserted HM1?", res)
    res = hash_map_2.insert(d3)
    print("Inserted HM2?", res)

    hprint("Table")
    pprint(hash_map_1._table)
    pprint(hash_map_2._table)

    hprint("Remove")
    print("key to remove:", d2.name)
    rem = hash_map_1.remove(d2.name)
    print("HM1", rem)
    rem = hash_map_2.remove(d2.name)
    print("HM2", rem)

    hprint("Table")
    pprint(hash_map_1._table)
    pprint(hash_map_2._table)


if __name__ == "__main__":
    main()
