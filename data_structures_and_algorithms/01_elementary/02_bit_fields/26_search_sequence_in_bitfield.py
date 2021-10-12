

if __name__ == '__main__':
    a = 0b_0011_0100_0100_1011
    NO_OF_BYTES = 2
    NBi = NO_OF_BITS = 8 * NO_OF_BYTES
    print(f"A {a:#0{10}b}")

    TERM = 0b1101
    TERM_SIZE = 4
    MASK = 2**TERM_SIZE - 1
    print(f"TERM {TERM:#0{TERM_SIZE + 2}b}")

    found: bool = False
    for i in range(NO_OF_BITS - TERM_SIZE + 1):
        e = extraction = (a & (MASK << i))
        st = shifted_term = TERM << i
        result: bool = extraction == shifted_term

        print(f"[{i: >2}] {e:#0{2+NBi}b} == {st:#0{2+NBi}b}: {result}")

        if result:
            found = True
            break

    if found:
        print(f"Found at offset {i}")
