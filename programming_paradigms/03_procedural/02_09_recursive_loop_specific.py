

def loop_instruction_forward(limit: int, i: int = 0) -> None:
    if i >= limit:  # this will break the loop
        return

    print(f"some_instruction #{i}")
    loop_instruction_forward(limit, i=i+1)


def loop_instruction_backward(limit: int, i: int = 0) -> None:
    if i >= limit:  # this will break the loop
        return

    loop_instruction_backward(limit, i=i+1)
    print(f"some_instruction #{i}")


if __name__ == '__main__':
    print("Loop forward")
    loop_instruction_forward(3)

    print("\nLoop backward")
    loop_instruction_backward(3)
