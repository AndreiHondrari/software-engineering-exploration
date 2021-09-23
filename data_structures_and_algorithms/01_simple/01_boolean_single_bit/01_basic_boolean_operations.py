

def apply_combinations(
    name,
    callback
):
    COMBINATIONS = [
        (False, False,),
        (False, True,),
        (True, False,),
        (True, True,),
    ]

    for c in COMBINATIONS:
        result: bool = callback(c[0], c[1])
        print(f"[{name}]: {result}")


if __name__ == '__main__':
    apply_combinations("Idempotence a+a", lambda a, b: a)
