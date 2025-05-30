def read_lists(filename: str) -> tuple[list[int], list[int]]:
    with open(filename) as f:
        l1_vals, l2_vals = zip(*(line.split() for line in f))
        l1 = [int(l1_val) for l1_val in l1_vals]
        l2 = [int(l2_val) for l2_val in l2_vals]
    return l1, l2


def find_dist(l1: list[int], l2: list[int]) -> int:
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)
    return sum((abs(x-y) for x, y in zip(l1_sorted, l2_sorted)))


def get_similarity_score(l1: list[int], l2: list[int]) -> int:
    total_score = 0
    for num in l1:
        total_score += num * (len([x for x in l2 if x == num]))
    return total_score


l1, l2 = read_lists("../../inputs/example_day01")
dist = find_dist(l1, l2)
score = get_similarity_score(l1, l2)
print(dist)
print(score)
