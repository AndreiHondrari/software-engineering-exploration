

def generate_unique_combinations(
    values: tuple[int],
    offset: int = 0,
    selection: tuple[int] = tuple()
) -> tuple[tuple[int]]:

    result = tuple()

    for i in range(offset, len(values)):
        new_selection = selection + (values[i],)
        result += (new_selection,)
        result += generate_unique_combinations(values, i + 1, new_selection)

    return result


def find_valid_combinations(
    reference_sum: int,
    combo: tuple[int],
    selection: tuple[int] = tuple()
) -> tuple[tuple[int]]:
    print()
    print("SELECTION\t", selection, end=" ")
    computed_sum = sum(selection)

    # handle leaf cases
    if computed_sum > reference_sum:
        print("---> FAIL", end=" ")
        return tuple()
    elif computed_sum == reference_sum:
        print("---> MATCH", end=" ")
        return (selection,)

    # build progress cases
    result = tuple()

    for x in combo:
        new_selection = selection + (x,)
        result += find_valid_combinations(reference_sum, combo, new_selection)

    return result


def find_coin_combinations(sum: int, coins: set[int]) -> tuple[tuple[int]]:
    immutable_coins = tuple(coins)
    combinations: tuple[tuple[int]] = generate_unique_combinations(
        immutable_coins
    )

    result = tuple()

    for combo in combinations:
        print()
        print()
        print("#" * 20)
        print("COMBO\t\t", combo)
        result += find_valid_combinations(sum, combo)

    return result


def main() -> None:
    sample_1 = (4, {1, 2, 3})
    sample_2 = (10, {2, 5, 3, 6})

    CASE = sample_2

    reference_sum = CASE[0]
    coins = CASE[1]

    result = find_coin_combinations(reference_sum, coins)

    print()
    print("-" * 10, "RESULT", "-" * 10)
    unique_coin_combinations = {}
    for r in result:
        sorted_r = tuple(sorted(r))
        print(sorted_r)
        if sorted_r not in unique_coin_combinations:
            unique_coin_combinations[sorted_r] = None

    print()
    print("-" * 10, "FINAL COUNT", "-" * 10)
    print(len(unique_coin_combinations))


if __name__ == "__main__":
    main()
