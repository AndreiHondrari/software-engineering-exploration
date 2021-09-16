from typing import Callable


def do_something() -> None:
    print("does_something")


def use_do_something(some_function: Callable[[], None]) -> None:
    some_function()


def retrieve_function() -> Callable[[], None]:
    return do_something


def retrieve_a_closure() -> Callable[[], None]:
    def new_function() -> None:
        print("new_something")
    return new_function


if __name__ == '__main__':

    # save function to variable
    print("Save function to variable")
    saved_function_1 = do_something
    saved_function_1()  # call it

    print("\nPass a function to another function")
    use_do_something(do_something)

    print("\nReceive a function from another function")
    saved_function_2 = retrieve_function()
    saved_function_2()

    print("\nGenerate a closure")
    saved_function_3 = retrieve_a_closure()
    saved_function_3()
