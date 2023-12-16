import input_reader as ir
from itertools import product
import re

def filler(word):
    options = [(c,) if c != "?" else (".", "#") for c in word]
    return list((''.join(o) for o in product(*options)))

def puzzle_1_old(input):
    possibilities = 0
    for idx, line in enumerate(input):
        print("{}/{}".format(idx + 1, len(input)))
        condition, broken_pieces = line.split()
        broken_pieces = [int(s) for s in broken_pieces.split(",")]

        combinations = filler(condition)
        for combination in combinations:
            if [len(s) for s in re.findall("#+", combination)] == broken_pieces:
                possibilities += 1

    print(possibilities)

def puzzle_1(input):
    possibilities = 0
    for idx, line in enumerate(input):
        print("{}/{}".format(idx + 1, len(input)))
        condition, broken_pieces = line.split()
        broken_pieces = [int(s) for s in broken_pieces.split(",")]


        combinations = remove_invalid_positions(condition)
        #combinations = filler(condition)
        for combination in combinations:
            if [len(s) for s in re.findall("#+", combination)] == broken_pieces:
                possibilities += 1

    print(possibilities)

def remove_invalid_positions(condition, broken_pieces):
    for piece_len in broken_pieces:
        for idx, s in condition:
            if s == "#":


def puzzle_2(input):
    total = 0
    for idx, line in enumerate(input):
        possibilities = 0
        other_possibilities = 0
        print("{}/{}".format(idx + 1, len(input)))
        condition, broken_pieces = line.split()
        broken_pieces = [int(s) for s in broken_pieces.split(",")]

        if  condition[0] == "#" and condition[1] == "#":
            continue

        combinations = filler(condition)
        for idx, combination in enumerate(combinations):
            if [len(s) for s in re.findall("#+", combination)] == broken_pieces:
                possibilities += 1


        for idx, combination in enumerate(combinations):
            new_condition = combination
            if combination[-1] == "#":
                new_condition = "." + new_condition
            else:
                new_condition = "?" + new_condition

            new_combinations = filler(new_condition)
            for com in new_combinations:
                if [len(s) for s in re.findall("#+", com)] == broken_pieces:
                    other_possibilities += 1

        this_round = possibilities * other_possibilities * other_possibilities* other_possibilities* other_possibilities
        print(this_round)
        total += this_round

    print(total)


if __name__ == "__main__":
    input = ir.read_test_input_lines()
    #puzzle_1(input)
    puzzle_2(input)
