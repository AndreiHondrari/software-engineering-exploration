
if __name__ == '__main__':
    not_apply_mask: int = 0
    apply_mask: int = 1

    a = 0x95
    MASK = 0x0F

    """
    -0 = 0000 0000
    -1 = 1111 1111
    """
    x = a | (-not_apply_mask & MASK)
    y = a | (-apply_mask & MASK)

    print(f"INITIAL     {a:#0{10}b}")
    print(f"MASK        {MASK:#0{10}b}")
    print(f"NOT APPLY   {x:#0{10}b}")
    print(f"APPLY       {y:#0{10}b}")
