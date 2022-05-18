from typing import Dict

TRUTH_MASK: Dict[bool, int] = {
    False: 0,
    True: 0xffffff
}

if __name__ == '__main__':

    a: int = 11
    b: int = 22

    condition1 = True
    condition2 = False

    x = (a & TRUTH_MASK[condition1]) | (b & TRUTH_MASK[(not condition1)])
    print(f"#1 {x}")

    x = (a & TRUTH_MASK[condition2]) | (b & TRUTH_MASK[(not condition2)])
    print(f"#2 {x}")
