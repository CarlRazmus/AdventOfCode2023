import input_reader as ir


def get_connected_neighbours(pos, map):
    curr_x, curr_y = pos
    neighbours = []
    curr_tile = map[curr_y][curr_x]

    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = dir
        next_y = curr_y + y
        next_x = curr_x + x

        if next_y in range(0, len(map)) and next_x in range(0, len(map[0])):
            next_tile = map[next_y][next_x]
            if is_connected(curr_tile, next_tile, dir):
                neighbours.append((next_x, next_y))

    return neighbours

def is_connected(curr_tile, next_tile, dir):
    x, y = dir
    if y == -1:
        if curr_tile in ["|", "J", "L", "S"]:
            if next_tile in ["|", "7", "F"]:
                return True
    if y == 1:
        if curr_tile in ["|", "7", "F", "S"]:
            if next_tile in ["|", "L", "J"]:
                return True
    if x == -1:
        if curr_tile in ["-", "J", "7", "S"]:
            if next_tile in ["-", "L", "F"]:
                return True
    if x == 1:
        if curr_tile in ["-", "L", "F", "S"]:
            if next_tile in ["-", "J", "7"]:
                return True
    return False

def find_start_node(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "S":
                return (x, y)

def puzzle_1(map):
    start_node = find_start_node(map)
    que = [start_node]
    loop_nodes = []
    while len(que) > 0:
        curr_node = que.pop()
        loop_nodes.append(curr_node)
        neighbours = get_connected_neighbours(curr_node, map)
        for neighbour in neighbours:
            if neighbour not in loop_nodes:
                que.append(neighbour)

    print((int(len(loop_nodes) - 1) / 2))
    return loop_nodes

def get_all_neighbours(pos, map):
    curr_x, curr_y = pos
    neighbours = []

    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = dir
        next_y = curr_y + y
        next_x = curr_x + x

        if next_y in range(0, len(map)) and next_x in range(0, len(map[0])):
            neighbours.append((next_x, next_y))
    return neighbours


def puzzle_2(map, loop_nodes):
    enclosed_node_groups = []
    nodes_left_to_search = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if (x, y) not in loop_nodes:
                nodes_left_to_search.append((x, y))

#    while len(nodes_left_to_search) > 0:
#        is_enclosed = True
#        start_node = nodes_left_to_search.pop()
#        group = [start_node]
#        que = [start_node]
#
#        while len(que) > 0:
#            node = que.pop()
#            x, y = node
#            if y == 0 or y == (len(map) - 1) or x == 0 or x == (len(map[0]) - 1):
#                is_enclosed = False
#
#            neighbours = [n for n in get_all_neighbours(node, map) if n in nodes_left_to_search]
#            for neighbour in neighbours:
#                nodes_left_to_search.remove(neighbour)
#                que.append(neighbour)
#                group.append(neighbour)
#        if is_enclosed:
#            enclosed_node_groups.append(group)
#
#    new_groups = remove_incorrect_groups(enclosed_node_groups, loop_nodes, map)
#    print(sum(len(group) for group in new_groups))

    cnt = 0
    for node in nodes_left_to_search:
        if is_within_loop(node, loop_nodes, map):
            cnt += 1

    print(cnt)

def is_within_loop(node, loop_nodes, map):
    if node == (7, 4):
        print("#oing")

    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x_diff, y_diff = dir
        x, y = node
        previous_node = node
        x = x + x_diff
        y = y + y_diff
        cnt = 0
        start_tile = None
        while y in range(len(map)) and x in range(len(map[0])):
            if (x, y) in loop_nodes:
                curr_tile = map[y][x]
                if curr_tile == "S":
                    curr_tile = "-"
                previous_tile = map[previous_node[1]][previous_node[0]]

                if previous_tile == "S":
                    previous_tile = "-"

                if is_connected(previous_tile, curr_tile, dir):
                    if curr_tile not in ["|", "-"]:
                        if y_diff == 1:
                            if (start_tile == "F" and curr_tile == "L") or (start_tile == "7" and curr_tile == "J"):
                                cnt += 1
                        elif y_diff == -1:
                            if (start_tile == "L" and curr_tile == "F") or (start_tile == "J" and curr_tile == "7"):
                                cnt += 1
                        elif x_diff == 1:
                            if (start_tile == "L" and curr_tile == "J") or (start_tile == "F" and curr_tile == "7"):
                                cnt += 1
                        elif x_diff == -1:
                            if (start_tile == "J" and curr_tile == "L") or (start_tile == "7" and curr_tile == "F"):
                                cnt += 1
                else:
                    start_tile = curr_tile
                    cnt += 1

            previous_node = (x, y)
            x = x + x_diff
            y = y + y_diff
        if (cnt % 2 == 0):
            return False
    return True

def remove_incorrect_groups(groups, loop_nodes, map):
    good_groups = []
    for group in groups:
        if is_within_loop(group[0], loop_nodes, map):
            good_groups.append(group)
    return good_groups

if __name__ == "__main__":
    input = ir.read_input_lines()
    map = [[x for x in line] for line in input]
    loop_nodes = puzzle_1(map)
    puzzle_2(map, loop_nodes)
