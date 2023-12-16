import re
from collections import defaultdict
import math
import itertools


def puzzle_1(instructions, maps):
    idx = 0
    curr_key = "AAA"
    instr_len = len(instructions)
    while True:
        if curr_key == "ZZZ":
            print(idx)
            return idx
        instruction = instructions[idx % instr_len]
        if instruction == "R":
            curr_key = maps[curr_key][1]
        else:
            curr_key = maps[curr_key][0]
        idx += 1

def is_win(keys):
    for x in keys:
        if x[-1] != "Z":
            return False
    return True

def puzzle_2(instructions, maps):
    input_keys = [x for x, t in maps.items() if x[-1] == "A"]
    instr_len = len(instructions)
    z_map = defaultdict(list)
    left_maps = dict()
    right_maps = dict()
    RIGHT = "R"

    for input_key, val in maps.items():
        left_maps[input_key] = val[0]
        right_maps[input_key] = val[1]

    for input_key in input_keys:
        idx = 0
        key = input_key
        not_finished = True

        while not_finished:
            if key[-1] == "Z":
                print(idx)
                for z_index in z_map[input_key]:
                    if (idx % instr_len) == (z_index % instr_len):
                        not_finished = False
                z_map[input_key].append(idx)

            if instructions[idx % instr_len] == RIGHT:
                key = right_maps[key]
            else:
                key = left_maps[key]
            idx += 1
    print(z_map)

    list_combinations = list(itertools.product(*z_map.values()))
    lcms = [math.lcm(*l) for l in list_combinations]
    print(min(lcms))

if __name__ == "__main__":
    with open(f"inputs/day_8.txt", "r", encoding="UTF-8") as file:
        input = file.read().split("\n\n")
        instructions = input[0]
        unparsed_lines = input[1]
        d = dict()
        for line in re.findall("(\w\w\w) = \((\w\w\w), (\w\w\w)\)", unparsed_lines):
            x, y, z = line
            d[x] = (y, z)
        puzzle_1(instructions, d)
        puzzle_2(instructions, d)
