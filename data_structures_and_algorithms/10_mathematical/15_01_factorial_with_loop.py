

def factorial(n: int) -> int:
    assert n >= 0, "value must be zero or positive"
    if n <= 1:
        return 1

    result: int = 1
    while n > 1:
        result *= n
        n = n - 1

    return result


if __name__ == '__main__':
    for k in range(10 + 1):
        result = factorial(k)
        print(f"{k}! = {result}")
