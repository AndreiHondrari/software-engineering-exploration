from typing import List


if __name__ == '__main__':
    array1: List[int] = [
        11, 22, 33, 44, 55, 66, 77, 88, 99,
        110, 120, 130, 140, 150, 160, 170, 180
    ]

    N_AMOUNT: int = 5
    NPLET_SIZE: int = len(array1) // N_AMOUNT
    RESIDUE_SIZE: int = len(array1) - NPLET_SIZE * N_AMOUNT

    n_lists: List[List[int]] = []
    residues: List[int] = []

    # separate
    for k in range(N_AMOUNT):
        new_nplet: List[int] = []
        n_lists.append(new_nplet)

        for i in range(NPLET_SIZE):
            new_nplet.append(array1[NPLET_SIZE * k + i])

    # residue
    if RESIDUE_SIZE > 0:
        for i in range(RESIDUE_SIZE):
            residues.append(array1[NPLET_SIZE * N_AMOUNT + i])

    # display
    for n_list in n_lists:
        print(n_list)

    print(f"Residues: {residues}")
