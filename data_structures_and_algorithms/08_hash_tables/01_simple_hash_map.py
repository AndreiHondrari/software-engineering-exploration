
import functools

from dataclasses import dataclass
from typing import Dict, Optional


hprint = functools.partial(print, "\n#")


@dataclass
class Data:
    name: str
    x: int
    y: int


class HashMap:

    def __init__(self) -> None:
        self._table: Dict[int, Data] = {}

    def hash(self, characters: str) -> int:
        hash_index = 0

        for c in characters:
            hash_index += ord(c)

        return hash_index

    def contains(self, name: str) -> bool:
        hash_index = self.hash(name)
        return hash_index in self._table

    def get(self, name: str) -> Optional[Data]:
        hash_index = self.hash(name)
        return self._table.get(hash_index)

    def insert(self, data: Data) -> bool:
        if self.contains(data.name):
            return False

        hash_index = self.hash(data.name)
        self._table[hash_index] = data
        return True

    def remove(self, name: str) -> Optional[Data]:
        if not self.contains(name):
            return None

        hash_index = self.hash(name)
        dangling_data = self._table[hash_index]
        del self._table[hash_index]
        return dangling_data


def main() -> None:
    hash_map = HashMap()

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
    hash_map.insert(d1)
    hash_map.insert(d2)

    hprint("Keys in map")
    print(hash_map._table.keys())

    hprint("Get the ones from #1")
    x = hash_map.get(d1.name)
    print(x)
    x = hash_map.get(d2.name)
    print(x)

    hprint("Check if d3 is in")
    k = hash_map.contains(d3.name)
    print(k)
    print("if it's true, then it is obvious that there is a hashing conflict")

    hprint("Getting the wrong data (due to collision)")
    print("requested key:", d3.name)
    x = hash_map.get(d3.name)
    print(x)

    hprint("Insert data with colliding name")
    print(d3)
    res = hash_map.insert(d3)
    print("Inserted?", res)

    hprint("Keys in map")
    print(hash_map._table.keys())

    hprint("Remove")
    print("key to remove:", d1.name)
    y = hash_map.remove(d1.name)
    print("ret:", y)

    hprint("Keys in map")
    print(hash_map._table.keys())

    hprint("Remove with collision")
    print("key to remove:", d3.name)
    y = hash_map.remove(d3.name)
    print("ret:", y)

    hprint("Keys in map")
    print(hash_map._table.keys())


if __name__ == "__main__":
    main()
