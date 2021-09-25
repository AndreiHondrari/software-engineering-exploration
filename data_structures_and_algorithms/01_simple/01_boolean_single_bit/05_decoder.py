from typing import Tuple
from collections import namedtuple

BaudotResult = namedtuple(
    "BaudotResult", [
        'a', 'b', 'c', 'd', 'e', 'f',
        # 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        # 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'
    ]
)


def decode(
    x: bool,
) -> Tuple[bool, bool]:
    a = not x
    b = x
    return a, b


def decode_baudot(
    p1: bool,
    p2: bool,
    p3: bool,
    p4: bool,
    p5: bool
):
    return BaudotResult(
        a=p1,
        b=p3 & p4,
        c=p1 & p3 & p4,
        d=p1 & p2 & p3 & p4,
        e=p2,
        f=p2 & p3 & p4,
        # g=p2 & p4,
        # h=p1 & p2 & p4,
        # i=p2 & p3,
        # j=p1 & p4,
        # k=p1 & p4 & p5,
        # l=p1 & p2 & p4 & p5,
        # m=p2 & p4 & p5,
        # n=p2 & p3 & p4 & p5,
        # o=p1 & p2 & p3,
        # p=p1 & p2 & p3 & p4 & p5,
        # q=p1 & p3 & p4 & p5,
        # r=p3 & p4 & p5,
        # s=p3 & p5,
        # t=p1 & p3 & p5,
        # u=p1 & p3,
        # v=p1 & p2 & p3 & p5,
        # x=p2 & p5,
        # y=p3,
        # z=p1 & p2 & p5
    )


if __name__ == '__main__':
    print("decode F: ", decode(False))
    print("decode T: ", decode(True))

    print("baudot 10000: ", decode_baudot(True, False, False, False, False))
    print("baudot 00110: ", decode_baudot(False, False, True, True, False))
    print("baudot 10110: ", decode_baudot(True, False, True, True, False))
