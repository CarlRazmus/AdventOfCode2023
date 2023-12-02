import input_reader as ir
import re


def find_all(color, s):
    return [int(s) for s in re.findall("(\d+) " + color, s)]

def puzzle_1(lines):
    ids = []
    for l in lines:
        game_id = ir.regex_groups_int_cast("Game (\d+):", l)[0]
        if max(find_all("red", l)) > 12:
            continue
        if max(find_all("green", l)) > 13:
            continue
        if max(find_all("blue", l)) > 14:
            continue
        ids.append(game_id)
    print(sum(ids))

def puzzle_2(lines):
    pwrs = []
    for l in lines:
        r = max(find_all("red", l))
        g = max(find_all("green", l))
        b = max(find_all("blue", l))
        pwrs.append(r * g * b)
    print(sum(pwrs))

if __name__ == "__main__":
    inputs = ir.read_input_lines()
    puzzle_1(inputs)
    puzzle_2(inputs)