
from typing import List, Dict, Tuple
from collections import defaultdict


def is_valid_sudoku(board: List[List[str]]) -> bool:
    SIZE = 9
    EMPTY = '.'

    rows: Dict[int, List[str]] = defaultdict(list)
    cols: Dict[int, List[str]] = defaultdict(list)
    sections: Dict[Tuple[int, int], List[str]] = defaultdict(list)

    for row_index in range(SIZE):
        for col_index in range(SIZE):
            value = board[row_index][col_index]
            if value == EMPTY:
                continue

            rows[row_index].append(value)
            cols[col_index].append(value)

            section_x = col_index // 3
            section_y = row_index // 3
            sections[(section_x, section_y)].append(value)

    for row in rows.values():
        if len(set(row)) < len(row):
            return False

    for col in cols.values():
        if len(set(col)) < len(col):
            return False

    for section in sections.values():
        if len(set(section)) < len(section):
            return False

    return True


def main() -> None:
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    res = is_valid_sudoku(board)
    print(res)


if __name__ == "__main__":
    main()
