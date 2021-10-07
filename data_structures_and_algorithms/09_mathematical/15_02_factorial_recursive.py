

def factorial(n: int) -> int:
    assert n >= 0, "value must be zero or positive"
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    for k in range(10 + 1):
        result = factorial(k)
        print(f"{k}! = {result}")
