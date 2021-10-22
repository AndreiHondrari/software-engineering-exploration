from typing import List, Callable


def selection_sort(array: List[int]) -> List[int]:
    result_array: List[int] = array.copy()

    SIZE: int = len(result_array)

    for i in range(0, SIZE):
        for j in range(i + 1, SIZE):
            if result_array[i] > result_array[j]:
                temp: int = result_array[i]
                result_array[i] = result_array[j]
                result_array[j] = temp

    return result_array


def bucket_sort(
    array: List[int],
    buckets_amount: int,
    bucket_sorting_func: Callable[[List[int]], List[int]]
) -> List[int]:
    if len(array) == 0:
        return array

    buckets: List[List[int]] = [[] for _ in range(buckets_amount)]

    MAX_VAL: int = max(array)

    # distribute values in buckets proportional to the max value
    bucket_index: int
    for i in range(len(array)):
        bucket_index = int((buckets_amount - 1) * array[i] / MAX_VAL)
        buckets[bucket_index].append(array[i])

    result_array: List[int] = []
    for i in range(buckets_amount):
        buckets[i] = bucket_sorting_func(buckets[i])
        result_array += buckets[i]

    return result_array


if __name__ == '__main__':
    array1: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]
    print(f"A1 BEFORE: {array1}")
    array1 = bucket_sort(array1, 3, selection_sort)
    print(f"A1 AFTER:  {array1}")

    array2: List[int] = [29, 25, 3, 49, 9, 37, 21, 43]
    print(f"A1 BEFORE: {array2}")
    array2 = bucket_sort(array2, 3, selection_sort)
    print(f"A1 AFTER:  {array2}")
