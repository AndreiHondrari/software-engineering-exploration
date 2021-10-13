

if __name__ == '__main__':
    # have some values
    a = 0b_0010_0000
    b = 0b_0010_1100
    c = 0b_1000_0001

    # imprint them on a film
    d = 0x00
    d = d | a
    d = d | b
    d = d | c

    ref = c
    is_ref_recognized: bool = (d & ref) != 0b0

    print(f"A:      {a:0{8}b}")
    print(f"B:      {b:0{8}b}")
    print(f"C:      {c:0{8}b}\n")
    print(f"FILM:   {d:0{8}b}\n")
    print(f"C recognized: {is_ref_recognized}")
