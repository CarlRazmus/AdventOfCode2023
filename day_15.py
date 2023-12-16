import input_reader as ir
from collections import defaultdict
import re

def hash(w):
    current_hash = 0
    for s in w:
        current_hash += ord(s)
        current_hash = current_hash * 17
        current_hash = current_hash % 256
    return current_hash


def puzzle_1(input):
    print(sum([hash(line) for line in input]))

def puzzle_2(input):
    boxes = defaultdict(list)
    for line in input:
        if "=" in line:
            label, focal_length = line.split("=")
            box_nr = hash(label)
            add_lens_to_box(boxes[box_nr], label, focal_length)
        else:
            label = line.split("-")[0]
            box_nr = hash(label)
            remove_label_from_box(boxes[box_nr], label)
    print(sum([focus_power(box_id, l) for box_id, l in boxes.items()]))

def focus_power(box_id, box):
    return sum([(box_id + 1) * (idx + 1) * int(p[1]) for idx, p in enumerate(box)])

def add_lens_to_box(box, add_label, add_focal_length):
    for idx, (label, _) in enumerate(box):
        if label == add_label:
            box[idx] = (label, add_focal_length)
            return
    box.append((add_label, add_focal_length))

def remove_label_from_box(box, remove_label):
    for idx, (label, _) in enumerate(box):
        if label == remove_label:
            box.pop(idx)
            return

if __name__ == "__main__":
    input = ir.read_input().rstrip("\n").split(",")
    puzzle_1(input)
    puzzle_2(input)
