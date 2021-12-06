
import asyncio

from typing import Coroutine, Any


async def do_something() -> None:
    print("START DO SOMETHING")
    await asyncio.sleep(1)
    print("DONE WAITING")


def main() -> None:
    print("Create one instance of the coroutine")
    coroutine: Coroutine[Any, Any, None] = do_something()

    print("Run coroutine #1")
    asyncio.run(coroutine)

    print("Run coroutine #2")
    try:
        asyncio.run(coroutine)
    except RuntimeError as rerr:
        print("Caught runtime error:", repr(rerr))

    print("DONE")


if __name__ == '__main__':
    main()
