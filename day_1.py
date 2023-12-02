import input_reader as ir
import re

def convert(s):
    if s == "one":
        return "1"
    elif s == "two":
        return "2"
    elif s == "three":
        return "3"
    elif s == "four":
        return "4"
    elif s == "five":
        return "5"
    elif s == "six":
        return "6"
    elif s == "seven":
        return "7"
    elif s == "eight":
        return "8"
    elif s == "nine":
        return "9"
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
