

def is_power_of_two(value: int) -> bool:
    return (
        (value != 0) and (
            (value & (value - 1)) == 0b0
        )
    )


if __name__ == '__main__':
    for i in range(16+1):
        result = is_power_of_two(i)
        print(f"{i}: {result}")
