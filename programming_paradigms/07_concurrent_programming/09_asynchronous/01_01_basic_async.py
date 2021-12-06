
import random
import asyncio

from typing import Coroutine, Any


async def do_something() -> int:
    print("START DO SOMETHING")
    await asyncio.sleep(1)
    print("DONE WAITING")

    return random.randint(1000, 10_000)


def main() -> None:
    print("Create coroutine")
    coroutine: Coroutine[Any, Any, int] = do_something()

    print("Run coroutine")
    result: int = asyncio.run(coroutine)

    print(f"DONE: {result}")


if __name__ == '__main__':
    main()
