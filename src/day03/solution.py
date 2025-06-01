import re


def read_file(filename):
    with open(filename) as f:
        return f.read()


def match_patterns(content):
    pattern = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.findall(pattern, content)
    return matches


def compute_muls(matches):
    return sum(int(a) * int(b) for a, b in matches)


content = read_file("../../inputs/day03.txt")
patterns = match_patterns(content)
print(compute_muls(patterns))
