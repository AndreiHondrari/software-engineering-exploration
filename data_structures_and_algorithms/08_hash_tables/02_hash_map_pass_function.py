
import functools

from dataclasses import dataclass
from typing import Dict, Optional, Callable


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
        self._table: Dict[int, Data] = {}
        self._hash_function = functools.lru_cache(hash_function)

    def contains(self, name: str) -> bool:
        hash_index = self._hash_function(name)
        return hash_index in self._table

    def get(self, name: str) -> Optional[Data]:
        hash_index = self._hash_function(name)
        return self._table.get(hash_index)

    def insert(self, data: Data) -> bool:
        if self.contains(data.name):
            return False

        hash_index = self._hash_function(data.name)
        self._table[hash_index] = data
        return True

    def remove(self, name: str) -> Optional[Data]:
        if not self.contains(name):
            return None

        hash_index = self._hash_function(name)
        dangling_data = self._table[hash_index]
        del self._table[hash_index]
        return dangling_data


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

    hprint("Keys in map")
    print(hash_map_1._table.keys())
    print(hash_map_2._table.keys())

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

    hprint("Keys in map")
    print("HM1", hash_map_1._table.keys())
    print("HM2", hash_map_2._table.keys())


if __name__ == "__main__":
    main()
