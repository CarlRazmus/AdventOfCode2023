import input_reader as ir
import pprint as pp
from collections import defaultdict
import functools
import re
import itertools

def get_hand_value_2(hand):
    best_score = 0
    if "J" in hand:
        if hand == "JJJJJ":
            return get_hand_value("AAAAA")

        sub_hand = hand.replace("J", "")
        chars = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        chars_lists = [chars for _ in range(hand.count("J"))]
        combinations = itertools.product(*chars_lists)

        for combo in combinations:
            score = get_hand_value(sub_hand + "".join(combo))
            if score > best_score:
                best_score = score
        return best_score
    else:
        return get_hand_value(hand)

def get_hand_value(hand):
    sorted_hand = sorted(hand)
    m = defaultdict(int)
    for card in sorted_hand:
        m[card] += 1

    #high card
    if len(m.keys()) == 5:
        return 1
    #one pair
    if len(m.keys()) == 4:
        return 2
    #two pair or three of a kind
    if len(m.keys()) == 3:
        for nr_of_a_kind in m.values():
            if nr_of_a_kind == 3:
                #three of a kind
                return 4
        #two pairs
        return 3

    #two pair or three of a kind
    if len(m.keys()) == 2:
        for nr_of_a_kind in m.values():
            if nr_of_a_kind == 4:
                #four of a kind
                return 6
        #full house
        return 5

    if len(m.keys()) == 1:
        return 7


def translate(letter):
    table = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    table.reverse()
    return table.index(letter)

def translate_2(letter):
    table = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    table.reverse()
    return table.index(letter)

def comp_cards(hand1_and_bid, hand2_and_bid):
    hand1 = hand1_and_bid[0]
    hand2 = hand2_and_bid[0]
    for idx in range(5):
        if hand1[idx] != hand2[idx]:
            return translate(hand1[idx]) - translate(hand2[idx])

def comp_cards_2(hand1_and_bid, hand2_and_bid):
    hand1 = hand1_and_bid[0]
    hand2 = hand2_and_bid[0]
    for idx in range(5):
        if hand1[idx] != hand2[idx]:
            return translate_2(hand1[idx]) - translate_2(hand2[idx])

def puzzle_1(input):
    hands_in_priorities = defaultdict(list)
    for line in input:
        hand, bid = line.split(" ")
        priority = get_hand_value(hand)
        hands_in_priorities[priority].append((hand, bid))

    rank = 1
    winnings = []
    for idx in range(0, 8):
        hands_and_bids = hands_in_priorities[idx]
        sorted_hands = sorted(hands_and_bids, key=functools.cmp_to_key(comp_cards))
        for hand_and_bid in sorted_hands:
            bid = hand_and_bid[1]
            winnings.append(int(bid) * rank)
            rank += 1

    pp.pprint(sum(winnings))

def puzzle_2(input):
    hands_in_priorities = defaultdict(list)
    for line in input:
        hand, bid = line.split(" ")
        priority = get_hand_value_2(hand)
        hands_in_priorities[priority].append((hand, bid))

    rank = 1
    winnings = []
    for idx in range(0, 8):
        hands_and_bids = hands_in_priorities[idx]
        sorted_hands = sorted(hands_and_bids, key=functools.cmp_to_key(comp_cards_2))
        for hand_and_bid in sorted_hands:
            bid = hand_and_bid[1]
            winnings.append(int(bid) * rank)
            rank += 1

    pp.pprint(sum(winnings))

if __name__ == "__main__":
    input = ir.read_input_lines()
    puzzle_1(input)
    puzzle_2(input)
