"""
AoC 2024, day 03, parts 1 & 2
Processes instructions and multiplication patterns from input. No advanced regex magic, uses a simple state machine to apply enable/disable instructions.
"""

import re


PATTERN_MUL = r"mul\((-?\d+),(-?\d+)\)"
PATTERN_ENABLE = r"do\(\)"
PATTERN_DISABLE = r"don't\(\)"


def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def match_patterns(pattern: str, content: str) -> list[tuple[str, str]]:
    """Finds all mul(NUM,NUM) expressions."""
    return re.findall(pattern, content)


def compute_muls(matches: list[tuple[str, str]]) -> int:
    """Returns the sum of all multiplication pairs."""
    return sum(int(a) * int(b) for a, b in matches)


def find_and_compute_muls(pattern: str, content: str) -> dict[int, int]:
    """
    Finds all mul() patterns.
    Returns dict mapping mul() start index to the multiplication result.
    """
    res = re.finditer(pattern, content)
    return {m.start(): int(m.group(1)) * int(m.group(2)) for m in res}


def find_instructions(content: str) -> dict[int, str]:
    """
    Finds all instructions.
    Returns dict mapping instructions' indexes to 'enable' and 'disable'.
    """
    enables = {m.start(): "enable" for m in re.finditer(PATTERN_ENABLE, content)}
    disables = {m.start(): "disable" for m in re.finditer(PATTERN_DISABLE, content)}
    return enables | disables


def get_instructed_muls(muls: dict[int, int], instrs: dict[int, str]) -> int:
    """
    Traverses dict with muls and instructions by their position in input.
    Applies enable/disable logic for multiplication commands.
    """
    code = muls | instrs
    res = 0
    disabled = False
    for key in sorted(code):
        val = code[key]
        if val == "enable":
            disabled = False
        elif val == "disable":
            disabled = True
        elif not disabled:
            res += code[key]
    return res


if __name__ == "__main__":
    content = read_file("../../inputs/day03.txt")
    patterns = match_patterns(PATTERN_MUL, content)
    print(compute_muls(patterns))  # Part 1

    muls = find_and_compute_muls(PATTERN_MUL, content)
    instrs = find_instructions(content)
    print(get_instructed_muls(muls, instrs))  # Part 2
