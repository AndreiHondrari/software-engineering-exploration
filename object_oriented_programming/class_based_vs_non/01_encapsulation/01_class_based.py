

class MyClass:

    def __init__(self) -> None:
        self.a = 11

    def do_something(self) -> None:
        self.a *= 2


if __name__ == '__main__':
    my_obj = MyClass()
    my_obj.do_something()
    print(my_obj.a)
