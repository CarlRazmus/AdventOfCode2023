import input_reader as ir
import re

def convert(s):
    l = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if s in l:
        return str(l.index(s))
    else:
        return s

def puzzle_1(input):
    nrs = [re.findall(r'\d', l) for l in input]
    nrs = [int(l[0] + l[-1]) for l in nrs]
    print(sum(nrs))

def puzzle_2(input):
    nrs = [re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', l) for l in input]
    nrs = [int(convert(l[0])+convert(l[-1])) for l in nrs]
    print(sum(nrs))

if __name__ == "__main__":
    input = ir.read_input_lines()
    puzzle_1(input)
    puzzle_2(input)
