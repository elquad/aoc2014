import re


pattern = r"mul\((-?\d+),(-?\d+)\)"
enablers = r"do\(\)"
disablers = r"don't\(\)"


def read_file(filename):
    with open(filename) as f:
        return f.read()


def match_patterns(content):
    matches = re.findall(pattern, content)
    return matches


def compute_muls(matches):
    return sum(int(a) * int(b) for a, b in matches)


def find_and_compute_muls(pattern, content):
    res = re.finditer(pattern, content)
    return {m.start(): int(m.group(1)) * int(m.group(2)) for m in res}


def find_instructions(content):
    res1 = re.finditer(enablers, content)
    res2 = re.finditer(disablers, content)
    return {m.start(): "enable" for m in res1} | {m.start(): "disable" for m in res2}


def get_instructed_muls(muls: dict[int, int], instrs: dict[int, str]) -> int:
    d = muls | instrs
    res = 0
    disabled = False
    for key in sorted(d):
        val = d[key]
        if val == "enable":
            disabled = False
            continue
        if disabled:
            continue
        if val == "disable":
            disabled = True
            continue
        res += d[key]
    return res


if __name__ == "__main__":
    content = read_file("../../inputs/day03.txt")
    patterns = match_patterns(content)
    print(compute_muls(patterns))  # Part 1

    muls = find_and_compute_muls(pattern, content)
    instrs = find_instructions(content)
    print(get_instructed_muls(muls, instrs))  # Part 2
