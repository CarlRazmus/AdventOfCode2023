import input_reader as ir
import pprint
import copy

def get_reduced_list(l):
    l1 = l[:-1]
    l2 = l[1:]
    return [e2 - e1 for e1, e2 in zip(l1, l2)]

def get_expanded_histories(lists):
    l_r = list(reversed(lists))
    for i in range(len(l_r) - 1):
        l1 = l_r[i]
        l2 = l_r[i + 1]
        l_r[i + 1].append(l1[-1] + l2[-1])
    return l_r

def get_expanded_previous_histories(lists):
    l_r = list(reversed(lists))
    for i in range(len(l_r) - 1):
        l1 = l_r[i]
        l2 = l_r[i + 1]
        l_r[i + 1].insert(0, l2[0] - l1[0])
    return l_r


def puzzle_1(puzzl1_1_input):
    sums = []
    for line in puzzl1_1_input:
        histories = [line]
        history = line
        while True:
            if len(set(history)) == 1:
                if 0 in set(history):
                    break
            history = get_reduced_list(history)
            histories.append(history)
        expanded_histories = get_expanded_histories(histories)
        sums.append(expanded_histories[-1][-1])

    print(sum(sums))


def puzzle_2(puzzle_input):
    sums = []
    for line in puzzle_input:
        histories = [line]
        history = line
        while True:
            if len(set(history)) == 1:
                if 0 in set(history):
                    break
            history = get_reduced_list(history)
            histories.append(history)
        expanded_histories = get_expanded_previous_histories(histories)
        sums.append(expanded_histories[-1][0])

    print(sum(sums))

if __name__ == "__main__":
    input = [[int(s) for s in line.split()] for line in ir.read_input_lines()]
    puzzle_1(copy.deepcopy(input))
    puzzle_2(copy.deepcopy(input))
