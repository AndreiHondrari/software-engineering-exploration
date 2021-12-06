
import random
import asyncio

from typing import List, Coroutine, Any


async def do_something() -> int:
    print("START DO SOMETHING")
    await asyncio.sleep(1)
    print("DONE WAITING")

    return random.randint(1000, 10_000)


def main() -> None:
    NO_OF_COROUTINES = 3
    print("Create coroutines")

    coroutines: List[Coroutine[Any, Any, int]] = []
    for i in range(NO_OF_COROUTINES):
        new_coroutine = do_something()
        coroutines.append(new_coroutine)

    print("Run coroutine")
    result: int = asyncio.run(coroutine)

    print(f"DONE: {result}")


if __name__ == '__main__':
    main()
