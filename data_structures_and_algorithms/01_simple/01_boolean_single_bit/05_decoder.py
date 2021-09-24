from typing import Tuple


def decode(
    x: bool,
) -> Tuple[bool, bool]:
    a = not x
    b = x
    return a, b


if __name__ == '__main__':
    print("decode F: ", decode(False))
    print("decode T: ", decode(True))
