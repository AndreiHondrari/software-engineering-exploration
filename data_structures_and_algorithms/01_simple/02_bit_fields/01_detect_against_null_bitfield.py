"""
Detect against null bitfield
"""

if __name__ == '__main__':
    a = 0b00000000
    b = 0b00100000

    a_is_null: bool = a == 0b0
    a_is_not_null: bool = a != 0b0

    b_is_null: bool = b == 0b0
    b_is_not_null: bool = b != 0b0

    print(f"a             {a:#0{10}b}")
    print(f"a_is_null     {a_is_null}")
    print(f"a_is_not_null {a_is_not_null}\n")

    print(f"b             {b:#0{10}b}")
    print(f"b_is_null     {b_is_null}")
    print(f"b_is_not_null {b_is_not_null}")
