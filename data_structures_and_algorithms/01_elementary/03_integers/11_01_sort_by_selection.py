"""
Perform selection sort by following the general algorithm:

iterate over complete collection:
    iterate over part of collection after current index of parent iterator
        compare elements of the two positions defined by the iterator indexes
            swap the values if they are not in order

The extraction of the digits as well as swapping are according
to the integer operations.
"""


def count_digits(n: int) -> int:
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


if __name__ == '__main__':
    a: int = 741672910385089
    no_of_digits: int = count_digits(a)

    x: int = a

    for i in range(no_of_digits):
        i_magnitude: int = 10**i
        for j in range(i+1, no_of_digits):
            j_magnitude: int = 10**j

            # extract digits
            i_digit: int = x // i_magnitude % 10
            j_digit: int = x // j_magnitude % 10

            if i_digit < j_digit:
                # swap digits
                old_at_i: int = i_digit * i_magnitude
                old_at_j: int = j_digit * j_magnitude

                new_at_i: int = j_digit * i_magnitude
                new_at_j: int = i_digit * j_magnitude

                x = x - old_at_i - old_at_j + new_at_i + new_at_j

    print(f"{a} -> {x}")
