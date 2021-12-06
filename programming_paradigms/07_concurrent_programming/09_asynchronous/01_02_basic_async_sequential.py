
import random
import asyncio

from typing import Coroutine, Any


async def do_something() -> int:
    print("START DO SOMETHING")
    await asyncio.sleep(1)
    print("DONE WAITING")

    return random.randint(1000, 10_000)


def main() -> None:
    coroutine: Coroutine[Any, Any, int]

    print("Run coroutine #1")
    coroutine = do_something()
    result: int = asyncio.run(coroutine)
    print(f"Result #1: {result}\n")

    print("Run coroutine #2")
    coroutine = do_something()
    result = asyncio.run(coroutine)
    print(f"Result #2: {result}\n")

    print("DONE")


if __name__ == '__main__':
    main()
