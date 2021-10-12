

if __name__ == '__main__':
    a: int = 123456789
    offset = 3

    x: int = a // 10**offset % 10
    y: int = (a % 10**(offset + 1)) // 10**offset

    # counting from 0 of course
    print(f"digit #{offset} from {a}")
    print(f"x: {x}")
    print(f"y: {y}")
