import input_reader as ir
import re


def get_adjacent_nrs(nrs, x, y):
    y_range = range(0, len(input))
    x_range = range(0, len(input[0]))
    adjacent_nrs = []

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            next_x = x + dx
            next_y = y + dy
            if next_x in x_range and next_y in y_range:
                for nr_and_range in nrs[next_y]:
                    if next_x in nr_and_range[1] and nr_and_range not in adjacent_nrs:
                        adjacent_nrs.append(nr_and_range)
    return adjacent_nrs

def get_gear_ratio(nrs, x, y):
    adjacent_nrs = get_adjacent_nrs(nrs, x, y)

    if len(adjacent_nrs) == 2:
        return adjacent_nrs[0][0] * adjacent_nrs[1][0]
    else:
        return 0

def get_nrs_and_ranges(input):
    nrs = []
    for y, line in enumerate(input):
        nrs.append([])
        curr_nr =""
        for x, s in enumerate(line):
            if s.isnumeric():
                curr_nr += s
            else:
                if curr_nr != "":
                    nrs[y].append((int(curr_nr), range(x - len(curr_nr), x), y))
                curr_nr =""
    return nrs

def puzzle_1(input, nrs):
    adjacent_nrs = set()
    for y, line in enumerate(input):
        for x, s in enumerate(line):
            if re.match("\d|\.|\n", s) == None:
                for nr_and_range in get_adjacent_nrs(nrs, x, y):
                    adjacent_nrs.add(nr_and_range)
    print(sum([nr_and_range[0] for nr_and_range in adjacent_nrs]))

def puzzle_2(input, nrs):
    gear_ratios = []
    for y, line in enumerate(input):
        for x, s in enumerate(line):
            if s == "*":
                gear_ratios.append(get_gear_ratio(nrs, x, y))
    print(sum(gear_ratios))

if __name__ == "__main__":
    input = ir.read_input_lines_dont_strip_newline()
    nrs = get_nrs_and_ranges(input)
    puzzle_1(input, nrs)
    puzzle_2(input, nrs)
