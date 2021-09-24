from typing import Tuple


def demux(
    i: bool,
    a: bool
) -> Tuple[bool, bool]:
    x = i & (not a)
    y = i & a
    return (x, y,)


if __name__ == '__main__':
    print("dmux F F", demux(False, False))
    print("dmux F T", demux(False, True))
    print("dmux T F", demux(True, False))
    print("dmux T T", demux(True, True))
