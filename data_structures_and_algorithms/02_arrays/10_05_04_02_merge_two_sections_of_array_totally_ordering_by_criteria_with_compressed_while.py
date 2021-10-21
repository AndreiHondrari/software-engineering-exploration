from typing import List


def merge_sections(
    source_array: List[int],
    section_1_start: int,
    section_1_end: int,
    section_2_start: int,
    section_2_end: int,
) -> List[int]:

    result_array: List[int] = []

    i: int = section_1_start
    j: int = section_2_start

    # distribute by comparison
    while i <= section_1_end or j <= section_2_end:
        if i <= section_1_end and (
            j > section_2_end or
            source_array[i] <= source_array[j]
        ):
            result_array.append(source_array[i])
            i += 1
        else:
            result_array.append(source_array[j])
            j += 1

    return result_array


if __name__ == '__main__':
    # notice they are of equal size
    source_array: List[int] = [
        11, 14, 17, 18, 19, 20, 22, 25, 29, 33, 42, 46, 52, 53, 54,
        66, 67, 68, 69, 70, 77
    ]
    SECTION_1_START: int = 2
    SECTION_1_END: int = 5
    SECTION_2_START: int = 9
    SECTION_2_END: int = 13

    print(f"INPUT: {source_array}\n")

    print(
        f"Section 1: {source_array[SECTION_1_START]} ... "
        f"{source_array[SECTION_1_END]}: "
        f"{source_array[SECTION_1_START:SECTION_1_END+1]}"
    )

    print(
        f"Section 2: {source_array[SECTION_2_START]} ... "
        f"{source_array[SECTION_2_END]}: "
        f"{source_array[SECTION_2_START:SECTION_2_END+1]}\n"
    )

    result: List[int] = merge_sections(
        source_array,
        SECTION_1_START, SECTION_1_END,
        SECTION_2_START, SECTION_2_END,
    )
    print(f"OUTPUT: {result}\n")

    result = merge_sections(
        source_array,
        SECTION_1_START, SECTION_2_START,
        SECTION_2_START + 1, SECTION_2_END,
    )
    print(f"OUTPUT: {result}\n")
