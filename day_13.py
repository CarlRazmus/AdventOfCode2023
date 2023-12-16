import input_reader as ir
import pprint

def number_mirrored(array):
    for start_idx in range(len(array) - 1):
        left = start_idx
        right = start_idx + 1

        mirror_found = True
        while left >= 0 and right < len(array):
            if array[left] != array[right]:
                mirror_found = False
                break
            left -= 1
            right += 1
        if mirror_found:
            return start_idx + 1
    return 0

def puzzle_1(patterns):
    columns_val = 0
    rows_val = 0
    for pattern in patterns:
        rows = [[s for s in line] for line in pattern]
        row_val = 100 * number_mirrored(rows)
        rows_val += row_val

        if row_val == 0:
            columns = [s for s  in zip(*rows)]
            columns_val += number_mirrored(columns)
    print(rows_val + columns_val)

def get_mirror_val(lines, invalid_pos):
    return number_mirrored_2(lines, invalid_pos)

    #if mirror_val != 0:
    #    if mirror_val - 1 != invalid_pos:
    #        print("found mirror at line {}".format(mirror_val - 1))
    #        return mirror_val
    #    else:
    #        print("already used value skipped at line {}".format(mirror_val - 1))
    #return 0

def number_mirrored_2(array, invalid_pos):
    for start_idx in range(len(array) - 1):
        left = start_idx
        right = start_idx + 1

        if foo(left, right, array):
            if start_idx != invalid_pos:
                return start_idx + 1
    return 0

def foo(left, right, array):
    while left >= 0 and right < len(array):
        if array[left] != array[right]:
            return False
        left -= 1
        right += 1
    return True

def find_for_all_combinations(pattern, invalid_pos):
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            print("pos ({},{})".format(x,y))
            new_pattern = [s for s in pattern]
            old_row = pattern[y]
            new_char = "." if old_row[x] == "#" else "#"
            new_row = old_row[:x] + new_char + old_row[x + 1:]
            new_pattern[y] = new_row
            #y == 6 should create new mirror at row 5
            rows = [[s for s in line] for line in new_pattern]

            row_val = get_mirror_val(rows, invalid_pos[0])
            if row_val > 0:
                return row_val * 100

            columns = [s for s  in zip(*rows)]
            col_val = get_mirror_val(columns, invalid_pos[1])
            if col_val > 0:
                return col_val

def puzzle_2(patterns):
    invalid_mirrors = []

    for pattern in patterns:
        rows = [[s for s in line] for line in pattern]
        row_val = number_mirrored(rows)
        if row_val != 0:
            invalid_mirrors.append((row_val-1, None))
        else:
            columns = [s for s in zip(*rows)]
            column_val = number_mirrored(columns)
            invalid_mirrors.append((None, column_val-1))

    mirror_vals = 0
    for idx, pattern in enumerate(patterns):
        print("patterns {}/{}".format(idx +1, len(patterns)))
        invalid_pos = invalid_mirrors[idx]
        mirror_vals += find_for_all_combinations(pattern, invalid_pos)
    print(mirror_vals)

if __name__ == "__main__":
    patterns = [[p for p in line.split()] for line in ir.read_input().split("\n\n")]
    #puzzle_1(patterns)
    puzzle_2(patterns)
