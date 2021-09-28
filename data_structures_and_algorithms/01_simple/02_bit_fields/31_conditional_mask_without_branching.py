

if __name__ == '__main__':
    not_apply_mask: int = 0
    apply_mask: int = 1

    a = 0x95
    MASK = 0xFF

    x = a ^ ((-not_apply_mask) & MASK)
    y = a ^ ((-apply_mask) & MASK)

    print(f"INITIAL     {a & 0xFF:#0{10}b}")
    print(f"NOT APPLY   {x & 0xFF:#0{10}b}")
    print(f"APPLY       {y & 0xFF:#0{10}b}")
