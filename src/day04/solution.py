"""
AoC 2024, day 04, part 1
Find horizontal, vertical, and diagonal occurences of WORD in the input.
"""


import operator
import re


WORD = "XMAS"
DIAGONALS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def count_diagonal_patterns(y: int, x: int, text: list[str]) -> int:
    """
    Finds count of the four possible diagonal patterns,
    makes sure negative slicing does not detect false positives.
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


def find_patterns(text: list[str]) -> int:
    horizontal = 0
    vertical = 0
    diagonal = 0

    for line in zip(*text):
        vertical += ''.join(line).count(WORD)
        vertical += ''.join(line[::-1]).count(WORD)
    for line_idx, line in enumerate(text):
        horizontal += line.count(WORD)
        horizontal += line.count(WORD[::-1])
        for char_idx, char in enumerate(line):
            if char == WORD[0]:
                diagonal += count_diagonal_patterns(line_idx, char_idx, text)

    return horizontal + vertical + diagonal


if __name__ == "__main__":
    with open("../../inputs/day04.txt") as f:
        print(find_patterns([line.strip() for line in f.readlines()]))  # Part 01
