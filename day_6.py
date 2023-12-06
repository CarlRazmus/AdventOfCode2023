import input_reader as ir
import re
import functools


def puzzle_1(input):
    answer = []
    for total_time, best_distance in input:
        winning_distances = []
        for time_waiting in range(total_time + 1):
            mm_per_sec = time_waiting
            time_left = total_time - time_waiting
            distance = mm_per_sec * time_left
            if distance > best_distance:
                winning_distances.append(time_waiting)
        answer.append(len(winning_distances))
    print(functools.reduce(lambda x, y: x*y, answer))


def puzzle_2(input):
    total_time, best_distance = input
    answer = []

    for time_waiting in range(total_time + 1):
        mm_per_sec = time_waiting
        time_left = total_time - time_waiting
        distance = mm_per_sec * time_left
        if distance > best_distance:
            answer.append(time_waiting)
            break

    for time_waiting in range(total_time + 1, 0, -1):
        mm_per_sec = time_waiting
        time_left = total_time - time_waiting
        distance = mm_per_sec * time_left
        if distance > best_distance:
            answer.append(time_waiting)
            break

    print(answer[1] - answer[0] + 1)

if __name__ == "__main__":
    input = ir.read_input_lines()

    times = re.findall("\d+", input[0])
    distances = re.findall("\d+", input[1])
    as_tuples = [(int(times[i]), int(distances[i])) for i in range(0, len(times))]

    puzzle_1(as_tuples)
    puzzle_2((int("".join(times)), int("".join(distances))))
