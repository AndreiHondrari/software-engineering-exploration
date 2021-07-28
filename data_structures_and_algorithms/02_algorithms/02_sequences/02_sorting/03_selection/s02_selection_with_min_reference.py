from typing import List

if __name__ == '__main__':

    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]

    print(f"Input array:  {array}")

    for i in range(0, len(array)):

        j_min: int = i  # assume smallest is the first

        for j in range(i+1, len(array)):

            if array[j] < array[j_min]:
                j_min = j

        if j_min != i:
            temporary_value = array[i]
            array[i] = array[j_min]
            array[j_min] = temporary_value
            print(f"{array} j_min={j_min}")

    print(f"Sorted array: {array}")
