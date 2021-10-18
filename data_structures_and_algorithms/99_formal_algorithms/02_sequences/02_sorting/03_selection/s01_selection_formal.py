from typing import List

if __name__ == '__main__':

    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]

    print(f"Input array:  {array}")

    for i in range(0, len(array)):

        for j in range(i+1, len(array)):

            if array[i] > array[j]:
                temporary_value = array[i]
                array[i] = array[j]
                array[j] = temporary_value
                print(array)

    print(f"Sorted array: {array}")
