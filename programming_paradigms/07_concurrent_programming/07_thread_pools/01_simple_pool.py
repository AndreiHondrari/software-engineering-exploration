import random
import threading
import functools
import concurrent.futures as futures

from typing import Callable, Any, Dict


def tprint(msg: str) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] {msg}", flush=True)


def mark_thread_ends(
    do_func: Callable[..., Any]
) -> Callable[..., Any]:

    @functools.wraps(do_func)
    def _inner(*args: Any, **kwargs: Any) -> Any:
        tprint("START")
        ret = do_func(*args, **kwargs)
        tprint("STOP")
        return ret

    return _inner


@mark_thread_ends
def do_something(value: int) -> int:
    tprint(f"VAL {value}")
    return value * 100


@mark_thread_ends
def main() -> None:
    executor = futures.ThreadPoolExecutor(max_workers=3)

    map_of_futures: Dict[futures.Future, int] = {}

    # initiate futures
    for _ in range(10):
        target_value = random.randint(1, 100)
        new_future = executor.submit(do_something, target_value)
        map_of_futures[new_future] = target_value

    # wait for futures and evaluate result
    for future_instance in futures.as_completed(map_of_futures):
        target_value = map_of_futures[future_instance]

        try:
            result = future_instance.result()
            tprint(
                f"Another one bites the dust: {target_value} -> {result}"
            )
        except Exception as exc:
            tprint(f"Oops {repr(exc)}")

    tprint("Shutting down executor ...")
    executor.shutdown()


if __name__ == '__main__':
    main()
