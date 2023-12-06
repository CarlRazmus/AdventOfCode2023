import input_reader as ir
import re
from collections import defaultdict

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def puzzle_1(input):
    win_points = []
    for _, winning_nrs, my_nrs in input:
        overlapping_nrs = intersection(winning_nrs, my_nrs)
        if (len(overlapping_nrs) > 0):
            win_points.append(pow(2, len(overlapping_nrs) - 1))
    print(sum(win_points))

def puzzle_2(input):
    card_copies = defaultdict(int)
    for card_nr, winning_nrs, my_nrs in input:
        overlapping_nrs = intersection(winning_nrs, my_nrs)
        card_copies[card_nr] += 1
        if (len(overlapping_nrs) > 0):
            for idx in range(len(overlapping_nrs)):
                nr_copies = card_copies[card_nr]
                card_copies[card_nr + idx + 1] += nr_copies
    print(sum([x for x in card_copies.values()]))

def parse_input(input):
    parsed_input = []
    for line in input:
        sides = line.split("|")
        card_nr = int(re.findall("\d+", sides[0].split(":")[0])[0])
        winning_nrs = re.findall("\d+", sides[0].split(":")[1])
        my_nrs = re.findall("\d+", sides[1])
        parsed_input.append((card_nr, winning_nrs, my_nrs))
    return parsed_input

if __name__ == "__main__":
    input = ir.read_input_lines()
    parsed_input = parse_input(input)
    puzzle_1(parsed_input)
    puzzle_2(parsed_input)