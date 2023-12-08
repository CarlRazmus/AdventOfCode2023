import input_reader as ir
import re


def puzzle_1(instructions, maps):
    idx = 0
    curr_key = next(iter(maps))
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


def puzzle_2(instructions, maps):
    print("part2")

if __name__ == "__main__":
    input = ir.read_input().split("\n\n")
    instructions = input[0]
    unparsed_lines = input[1]
    d = dict()
    for line in re.findall("(\w\w\w) = \((\w\w\w), (\w\w\w)\)", unparsed_lines):
        x, y, z = line
        d[x] = (y, z)
    puzzle_1(instructions, d)
    puzzle_2(instructions, d)
