import input_reader as ir
import pprint as pp
import re


def get_destination_value(val, map):
    for i in map:
        if val in i[0]:
            return val + i[1]
    return val

def puzzle_1(seeds, maps):
    que = seeds
    destination_nrs = []
    for map in maps:
        destination_nrs = []
        for val in que:
            destination_val = get_destination_value(int(val), map)
            destination_nrs.append(destination_val)
        que = destination_nrs
    print(sorted(destination_nrs)[0])

def puzzle_2(unparsed_seeds, maps):
    seed_ranges = re.findall("(\d+) (\d+)", unparsed_seeds)
    seed_ranges = [range(int(x), int(x) + int(y)) for x, y in seed_ranges]

    lowest_location = seed_ranges[0][0]
    for seed_range in seed_ranges:
        for idx, seed in enumerate(seed_range):
            if idx % 1000000 == 0:
                print(seed)

            val = seed
            for map in maps:
                for r, x in map:
                    if val in r:
                        val = val + x
                        break
            if val < lowest_location:
                lowest_location = val
    print(lowest_location)

if __name__ == "__main__":
    input = ir.read_input()
    parts = input.split("\n\n")
    seeds = re.findall("\d+", parts[0])
    maps = parts[1:]
    maps = [re.findall("(\d+) (\d+) (\d+)", map) for map in maps]
    parsed_input = []
    for map in maps:
        curr_map = []
        for destination, source, length in map:
            r = range(int(source), int(source) + int(length))
            diff = int(destination) - int(source)
            curr_map.append((r, diff))
        parsed_input.append(curr_map)

    puzzle_1(seeds, parsed_input)
    puzzle_2(parts[0], parsed_input)