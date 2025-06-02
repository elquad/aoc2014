"""
AoC 2024, day 04, parts 1 & 2
"Word puzzle"
"""


import re


WORD = "XMAS"
DIAGONALS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def count_x_mas_patterns(y: int, x: int, text: list[str]) -> int:
    """
    Finds count of 'MAS' written in self-crossing fashion.

    Args:
        y: Row index of the center coordinate.
        x: Column index of the center coordinate.
        text: List of strings, each representing a row of the grid.
    """
    count = 0
    if not (1 <= y < len(text)-1 and 1 <= x < len(text[0])-1):
        return 0
    if (
            (text[y-1][x-1] == "M" and text[y+1][x+1] == "S") or
            (text[y-1][x-1] == "S" and text[y+1][x+1] == "M")
        ) and (
            (text[y+1][x-1] == "M" and text[y-1][x+1] == "S") or
            (text[y+1][x-1] == "S" and text[y-1][x+1] == "M")):
        count += 1
    return count


def count_diagonal_patterns(y: int, x: int, text: list[str]) -> int:
    """
    Finds count of the four possible diagonal patterns,
    makes sure negative slicing does not detect false positives.

    Args:
        y: Row index of the first letter coordinate.
        x: Column index of the first letter coordinate.
        text: List of strings, each representing a row of the grid.
    """
    count = 0
    for dy, dx in DIAGONALS:
        if dy == 1 and y > len(text) - len(WORD):
            continue
        if dy == -1 and y < len(WORD) - 1:
            continue
        if dx == 1 and x > len(text[0]) - len(WORD):
            continue
        if dx == -1 and x < len(WORD) - 1:
            continue
        if all(text[y+dy*i][x+dx*i] == WORD[i] for i in range(1, len(WORD))):
            count += 1
    return count


def find_patterns(text: list[str]) -> tuple[int, int]:
    """
    Finds horizontal, vertical, and diagonal occurences of XMAS.
    Finds cross-wise occurences of MAS.
    """
    horizontal = 0
    vertical = 0
    diagonal = 0
    x_mas = 0

    for line in zip(*text):
        vertical += ''.join(line).count(WORD)
        vertical += ''.join(line[::-1]).count(WORD)
    for line_idx, line in enumerate(text):
        horizontal += line.count(WORD)
        horizontal += line.count(WORD[::-1])
        for char_idx, char in enumerate(line):
            if char == WORD[0]:
                diagonal += count_diagonal_patterns(line_idx, char_idx, text)
            if char == "A":
                x_mas += count_x_mas_patterns(line_idx, char_idx, text)

    return (horizontal + vertical + diagonal, x_mas)


if __name__ == "__main__":
    with open("../../inputs/day04.txt") as f:
        xmas, x_mas = find_patterns([line.strip() for line in f.readlines()])

print(xmas)  # Part 01
print(x_mas)  # Part 02
