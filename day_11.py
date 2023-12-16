import input_reader as ir
import pprint
from collections import defaultdict


def distance(n1, n2):
    return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

def puzzle_1(input, empty_rows, empty_cols):
    d = list()
    for y, line in enumerate(input):
        for x, e in enumerate(line):
            if e == "#":
                real_x = x + sum([1 for empty_c in empty_cols if x > empty_c])
                real_y = y + sum([1 for empty_r in empty_rows if y > empty_r])
                d.append((real_x, real_y))

    pairs = list()
    for idx, n1 in enumerate(d):
        for n2 in d:
            if n1 != n2: # and (n2, n1) not in pairs and (n1, n2) not in pairs:
                pairs.append((n1, n2))

    better_pairs = []
    cnt = 1
    while len(pairs) > 0:
        print("{}/{}".format(cnt, len(pairs)))
        cnt += 1
        n1, n2 = pairs.pop()
        if n1 != n2:
            better_pairs.append((n1, n2))
        if (n2, n1) in pairs:
            pairs.remove((n2, n1))
    paths = [distance(s1, s2) for s1, s2 in pairs]
    print(sum(paths))

def puzzle_2(input, empty_rows, empty_cols):
    print("part2")

if __name__ == "__main__":
    input = ir.read_input_lines()
    empty_rows=[idx for idx, row in enumerate(input) if set(row) == set(".")]
    empty_cols=[idx for idx, row in enumerate(zip(*input)) if set(row) == set(".")]

    puzzle_1(input, empty_rows, empty_cols)
    puzzle_2(input, empty_rows, empty_cols)
