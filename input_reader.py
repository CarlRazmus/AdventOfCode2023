import inspect
import re
import os
import requests


AOC_URL = "https://adventofcode.com/2023/day"

def puzzle_data_exists(day):
    return f"day_{day}.txt" in os.listdir("inputs")

def create_puzzle_data(day):
    print(f"creating new puzzle data for day {day}")
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', os.getenv("AOC_SESSION_COOKIE"))
    response = requests.get(f"{AOC_URL}/{day}/input", cookies=jar, timeout=5)

    if not response.ok:
        raise AssertionError("Response from adventOfCode server was not ok")

    with open(f"inputs/day_{day}.txt", "w", encoding="UTF-8") as file:
        file.write(response.text)

def get_current_day_and_generate_input_data():
    calling_file = [stack.filename for stack in inspect.stack() if "AdventOfCode" in stack.filename][-1]
    day = re.search(r"\d{1,2}", calling_file.split("\\")[-1]).group(0)

    if not puzzle_data_exists(day):
        create_puzzle_data(day)
    return day

def read_test_input():
    with open("inputs/test_data.txt", "r", encoding="UTF-8") as file:
        return file.read()

def read_test_input_lines():
    with open("inputs/test_data.txt", encoding="UTF-8") as file:
        return [line.rstrip('\n') for line in file]

def read_input():
    day = get_current_day_and_generate_input_data()

    with open(f"inputs/day_{day}.txt", "r", encoding="UTF-8") as file:
        return file.read()

def read_input_lines():
    day = get_current_day_and_generate_input_data()

    with open(f"inputs/day_{day}.txt", "r", encoding="UTF-8") as file:
        return [line.rstrip('\n') for line in file]



def get_lines_as_int(lines):
    return [int(c) for c in lines]

def get_lines_as_ints(lines):
    return [split_as_ints(line) for line in lines]

def get_lines_as_strings(lines, sep=None):
    return [line.split(sep) for line in lines]

def get_lines_with_regex(lines, expr, group_idx=0):
    return [regex(expr, l, group_idx) for l in lines]

def get_lines_with_regex_groups(lines, expr):
    return [regex_groups(expr, line) for line in lines]

def get_lines_with_regex_with_int_cast(lines, expr, group_idx=0):
    return [regex_int_cast(expr, line, group_idx) for line in lines]

def get_lines_with_regex_groups_int_cast(lines, expr):
    return [regex_groups_int_cast(expr, line) for line in lines]



def split_as_ints(line, sep=None):
    return [int(y) for y in line.split(sep)]

def regex(expr, line, group_idx=0):
    return [m.group(group_idx) for m in [re.search(expr, line)] if m]

def regex_int_cast(expr, line, group_idx=0):
    return [int(m.group(group_idx)) if m.group(group_idx).isnumeric() else m.group(group_idx) for m in [re.search(expr, line)] if m]

def regex_groups(expr, line):
    return [m.groups() for m in [re.search(expr, line)] if m]

def regex_groups_int_cast(expr, line):
    return [int(x) for x in re.search(expr, line).groups()]
