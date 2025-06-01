"""
AoC 2024, day 04, part 1
First sketch of the XMAS word search puzzle.
"""


import operator
import re


WORD = "XMAS"


def count_diagonal_patterns(y: int, x: int, text: list[str]) -> int:
    """
    Finds count of the four possible diagonal patterns,
    makes sure negative slicing does not detect false positives.
    """
    ops = {'+': operator.add, '-': operator.sub}
    count = 0
    for op1 in ops.keys():
        if op1 == '+' and y > len(text) - len(WORD) + 1:
            continue
        if op1 == '-' and y < len(WORD) - 1:
            continue
        for op2 in ops.keys():
            if op2 == '+' and x > len(text[0]) - len(WORD) + 1:
                continue
            if op2 == '-' and x < len(WORD) - 1:
                continue
            try:
                if all(text[ops[op1](y, i)][ops[op2](x, i)] == WORD[i] for i in range(1, len(WORD))):
                    count += 1
            except IndexError:
                pass
    return count


def find_patterns(text: list[str]) -> int:
    horizontal = 0
    vertical = 0
    diagonal = 0

    for line in zip(*text):
        vertical += len(re.findall(WORD, ''.join(line)))
        vertical += len(re.findall(WORD[::-1], ''.join(line)))
    for line_idx, line in enumerate(text):
        horizontal += len(re.findall(WORD, line))
        horizontal += len(re.findall(WORD[::-1], line))
        for char_idx, char in enumerate(line):
            if char == WORD[0]:
                diagonal += count_diagonal_patterns(line_idx, char_idx, text)

    return horizontal + vertical + diagonal


if __name__ == "__main__":
    with open("../../inputs/day04.txt") as f:
        print(find_patterns([line.strip() for line in f.readlines()]))
