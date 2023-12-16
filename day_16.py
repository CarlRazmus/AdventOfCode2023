import input_reader as ir
from collections import defaultdict


beams = dict()
traveled_pos = defaultdict(list)
width = 0

def puzzle_1(input):
    global beams
    global traveled_pos
    global width
    width = len(input)
    beams = dict()
    count = dict()
    for y, line in enumerate(input):
        for x, e in enumerate(line):
            beams[(x, y)] = e
            count[(x, y)] = 0

    travel((1,0), (0,0))
    print(len(traveled_pos))

def travel(dir, pos):
    global beams
    global traveled_pos
    global width

    while pos[0] in range(width) and pos[1] in range(width) and dir not in traveled_pos[pos]:
        traveled_pos[pos].append(dir)
        beam = beams[pos]

        if beam == ".":
            pos = add_tuples(pos, dir)

        elif beam == "-":
            if dir[1] == 0:
                pos = add_tuples(pos, dir)
            else:
                travel((-1, 0), add_tuples(pos, (-1, 0)))
                travel((1, 0), add_tuples(pos, (1, 0)))

        elif beam == "|":
            if dir[0] == 0:
                pos = add_tuples(pos, dir)
            else:
                travel((0, -1), add_tuples(pos, (0, -1)))
                travel((0, 1), add_tuples(pos, (0, 1)))

        elif beam == "\\":
            if dir == (1, 0):
                dir = (0, 1)
                pos = add_tuples(pos, dir)

            elif dir == (-1, 0):
                dir = (0, -1)
                pos = add_tuples(pos, dir)

            elif dir == (0, 1):
                dir = (1, 0)
                pos = add_tuples(pos, dir)

            elif dir == (0, -1):
                dir = (-1, 0)
                pos = add_tuples(pos, dir)

        elif beam == "/":
            if dir == (1, 0):
                dir = (0, -1)
                pos = add_tuples(pos, dir)

            elif dir == (-1, 0):
                dir = (0, 1)
                pos = add_tuples(pos, dir)

            elif dir == (0, 1):
                dir = (-1, 0)
                pos = add_tuples(pos, dir)

            elif dir == (0, -1):
                dir = (1, 0)
                pos = add_tuples(pos, dir)

def add_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def puzzle_2(input):
    global beams
    global traveled_pos
    global width
    width = len(input)
    beams = dict()
    for y, line in enumerate(input):
        for x, e in enumerate(line):
            beams[(x, y)] = e

    most_energized = 0
    for x in range(width):
        traveled_pos.clear()
        travel((0,1), (x,0))
        energized = len(traveled_pos)
        if energized > most_energized:
            most_energized = energized

    for x in range(width):
        traveled_pos.clear()
        travel((0,-1), (x,width-1))
        energized = len(traveled_pos)
        if energized > most_energized:
            most_energized = energized

    for y in range(width):
        traveled_pos.clear()
        travel((1,0), (0, y))
        energized = len(traveled_pos)
        if energized > most_energized:
            most_energized = energized

    for y in range(width):
        traveled_pos.clear()
        travel((-1,0), (width-1, y))
        energized = len(traveled_pos)
        if energized > most_energized:
            most_energized = energized
    print(most_energized)

if __name__ == "__main__":
    input = ir.read_input_lines()
    puzzle_1(input)
    puzzle_2(input)
