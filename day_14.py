import input_reader as ir
import pprint
import re
import time
import copy


def find_best_north_position(new_column):
    for idx in range(len(new_column)-1, -1, -1):
        if new_column[idx] == "#" or new_column[idx] == "O":
            return idx + 1
    return 0

def get_total_load(array):
    load = 0
    arr_len = len(array)
    for y, row in enumerate(array):
        load += sum([arr_len - y for e in row if e == "O"])
    return load

def move_round_stones_north(columns):
    new_array = []
    for column in columns:
        new_column = []
        for e in column:
            if e == "O":
                new_column.append(".")
                idx = find_best_north_position(new_column)
                new_column[idx] = "O"
            else:
                new_column.append(e)
        new_array.append(new_column)
    return new_array


def find_best_position(new_column):
    for idx in range(len(new_column)-1, -1, -1):
        if new_column[idx] == "#" or new_column[idx] == "O":
            return idx + 1
    return 0

def tilt_north(round_stones, square_stones):
    first_possible_position = list()
    for _ in range(len(round_stones)):
        first_possible_position.append(0)

    for row_idx in range(len(round_stones)):

        for stone_idx in square_stones[row_idx]:
            first_possible_position[stone_idx] = row_idx + 1

        for stone_idx in round_stones[row_idx]:

            if first_possible_position[stone_idx] < row_idx:
                round_stones[first_possible_position[stone_idx]].append(stone_idx)
                round_stones[row_idx] = [x for x in round_stones[row_idx] if x != stone_idx]
                first_possible_position[stone_idx] += 1
            else:
                first_possible_position[stone_idx] = row_idx + 1

def tilt_south(round_stones, square_stones):
    first_possible_position = list()
    for _ in range(len(round_stones) -1, -1, -1):
        first_possible_position.append(len(round_stones) - 1)

    for row_idx in range(len(round_stones) -1, -1, -1):

        for stone_idx in square_stones[row_idx]:
            first_possible_position[stone_idx] = row_idx - 1

        for stone_idx in round_stones[row_idx]:

            if first_possible_position[stone_idx] > row_idx:
                round_stones[first_possible_position[stone_idx]].append(stone_idx)
                round_stones[row_idx] = [x for x in round_stones[row_idx] if x != stone_idx]
                first_possible_position[stone_idx] -= 1
            else:
                first_possible_position[stone_idx] = row_idx - 1

def get_smallest_position(i, possible_pos, square_stones):

    if len(square_stones) == 0 or i < square_stones[0]:
        return possible_pos

    for idx, square_stone in enumerate(square_stones[1:]):
        if i < square_stone:
            return max(square_stones[idx] + 1, possible_pos)
    return max(square_stones[-1] + 1, possible_pos)

def get_biggest_position(i, possible_pos, square_stones):

    if len(square_stones) == 0 or i > square_stones[-1]:
        return possible_pos

    idx = len(square_stones) - 1
    for square_stone in reversed(square_stones[:-1]):
        if i > square_stone:
            return min(square_stones[idx] - 1, possible_pos)
        idx -= 1
    return min(square_stones[0] - 1, possible_pos)

def tilt_west(rows, square_stones):

    for idx, round_stones in enumerate(rows):
        last_position = -1
        new_row = []
        for e in sorted(round_stones):
            last_position = get_smallest_position(e, last_position + 1, square_stones[idx])
            new_row.append(last_position)
        rows[idx] = new_row

def tilt_east(rows, square_stones):

    for idx, round_stones in enumerate(rows):
        last_position = len(rows)
        new_row = []
        for e in reversed(sorted(round_stones)):
            last_position = get_biggest_position(e, last_position - 1, square_stones[idx])
            new_row.append(last_position)
        rows[idx] = new_row

def print_as_image(round_stones, square_stones, width):

    for y in range(width):
        row = ""
        for x in range(width):
            if x in round_stones[y]:
                row += "O"
            elif x in square_stones[y]:
                row += "#"
            else:
                row += "."
        print(row)
    print()

def get_total_load_optimized(round_stones):
    load = 0
    arr_len = len(round_stones)
    for y, row in enumerate(round_stones):
        load += sum([arr_len - y for _ in row])
    return load

def puzzle_2(input):
    round_stones = [[idx for idx, s in enumerate(line) if s == "O"] for line in input]
    square_stones = [[idx for idx, s in enumerate(line) if s == "#"] for line in input]
    width = len(input)

    print_as_image(round_stones, square_stones, width)
    round_stones_history = []
    start_time = time.time()
    for idx in range(131):
        if idx % 100000 == 0:
            print("{}/{}".format(idx, 1000000000))
            print("--- %s seconds ---" % (time.time() - start_time))
            start_time = time.time()
        tilt_north(round_stones, square_stones)
        tilt_west(round_stones, square_stones)
        tilt_south(round_stones, square_stones)
        tilt_east(round_stones, square_stones)
        for history in round_stones_history:
            if compare_lists(round_stones, history):
                print("oingoni")
        round_stones_history.append(copy.deepcopy(round_stones))

    #print an image in case something is wrong with calculations of load
    print_as_image(round_stones, square_stones, width)
    print()
    print(get_total_load_optimized(round_stones))

def compare_lists(round_stones, history):
    for idx, row in enumerate(round_stones):
        if row != history[idx]:
            return False
    return True

def puzzle_1(input):
    input_columns = [list(s) for s in list(zip(*input))]
    new_columns = move_round_stones_north(input_columns)
    row_array = [s for s in list(zip(*new_columns))]
    print(get_total_load(row_array))

if __name__ == "__main__":
    input = [[s for s in line] for line in ir.read_input_lines()]
    #puzzle_1(input)
    puzzle_2(input)
