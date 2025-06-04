"""
AoC 2024, day 05, part 1
"""


def process_file(filename: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    """
    Read the file containing:
        - list of rules in format NUM|NUM, where | is "precedes"
        - sequences of numbers
    """
    rules: dict[int, set] = {}
    with open(filename) as f:
        for line in f:
            if line == "\n":
                break
            a, b = map(int, line.strip().split('|'))
            rules.setdefault(a, set()).add(b)
        sequences = [
                [int(n) for n in x.split(',') if n]
                for x in [line.strip() for line in f]
                if x
        ]
    return rules, sequences


def validate_seq(rules: dict[int, set[int]], seq: list[int]) -> bool:
    """True if numbers in seq are ordered by the precedence rules."""
    for idx, num in enumerate(seq):
        ruleset = rules.get(num, None)
        if ruleset is not None:
            for num in ruleset:
                if num in seq and seq.index(num) < idx:
                    return False
    return True


def get_correct_seqs_mids(
        rules: dict[int, set[int]],
        sequences: list[list[int]]
        ) -> list[int]:
    """Validate the list of all sequences, return their midpoints."""
    mids = []
    for seq in sequences:
        if validate_seq(rules, seq):
            mids.append(seq[(len(seq) - 1) // 2])
    return mids


if __name__ == "__main__":
    rules, sequences = process_file("../../inputs/day05.txt")
    mids = get_correct_seqs_mids(rules, sequences)
    print(sum(mids))
