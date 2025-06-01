"""
AoC 2024, day 02, parts 1 & 2
Uses a custom iterator to provide a sliding window over integer sequences with optional skipping of a single element.
"""

from collections import deque


class SlidingPairs:
    """Yields consecutive pairs from the sequence, with optional skipping of a single element at the specified index."""
    def _advance_window(self) -> None:
        if self._skip_idx is not None and self._skip_idx == self._index:
            next(self._source)
        self._queue.append(next(self._source))
        self._index += 1

    def __init__(self, input_seq: str, skip_idx: int | None = None):
        self._skip_idx = skip_idx
        self._index = 0
        self._source = (int(x) for x in input_seq.split())
        self._queue = deque()
        self._stopped = False
        for x in range(2):
            try:
                self._advance_window()
            except StopIteration:
                raise ValueError("Input sequence too short")

    def __iter__(self) -> 'SlidingPairs':
        return self

    def __next__(self) -> tuple[int, int]:
        if self._stopped:
            raise StopIteration
        res = tuple(self._queue)
        self._queue.popleft()
        try:
            self._advance_window()
        except StopIteration:
            self._stopped = True
        return res


def is_pair_safe(diff: int, first_diff: int) -> bool:
    if diff == 0 or abs(diff) > 3:
        return False
    if diff > 0 and first_diff < 0:
        return False
    if diff < 0 and first_diff > 0:
        return False
    return True


def is_sequence_safe(line: str, permit_one_error: bool, skip_idx: int | None = None) -> bool:
    first_diff = None
    for idx, (a, b) in enumerate(SlidingPairs(line, skip_idx)):
        if first_diff is None:
            first_diff = a - b
        if not is_pair_safe(a - b, first_diff) and permit_one_error:
            if skip_idx is not None:
                return False  # second pass permits no unsafe pairs
            return any([
                    is_sequence_safe(line, True, idx-1),
                    is_sequence_safe(line, True, idx),
                    is_sequence_safe(line, True, idx+1)
            ])
        if not is_pair_safe(a - b, first_diff) and not permit_one_error:
            return False

    return True


def get_safe_count(filename: str, permit_one_error: bool) -> int:
    with open(filename) as f:
        return sum(is_sequence_safe(line, permit_one_error) for line in f)


if __name__ == "__main__":
    print(get_safe_count("../../inputs/day02.txt", False))
    print(get_safe_count("../../inputs/day02.txt", True))
