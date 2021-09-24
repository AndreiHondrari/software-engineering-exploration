from typing import Dict
from dataclasses import dataclass
from collections import namedtuple


ResultTuple = namedtuple("ResultTuple", ['a', 'b'])


@dataclass
class Result:
    a: int
    b: int


def obtain_dict() -> Dict[str, int]:
    return {
        'a': 11,
        'b': 22,
    }


def obtain_named_tuple() -> ResultTuple:
    return ResultTuple(a=33, b=44)


def obtain_dataclass() -> Result:
    return Result(a=55, b=66)


if __name__ == '__main__':
    print("Values from dictionary result")
    res1 = obtain_dict()
    a1 = res1['a']
    b1 = res1['b']
    print(f"{a1} {b1}")

    print("\nValues from named tuple")
    res2 = obtain_named_tuple()
    a2: int = res2.a
    b2: int = res2.b
    print(f"{a2} {b2}")

    print("\nValues from dataclass")
    res3 = obtain_dataclass()
    a3: int = res3.a
    b3: int = res3.b
    print(f"{a3} {b3}")
