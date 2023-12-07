#!/usr/bin/env python

from collections import Counter

def card_to_num(card):
    if card.isnumeric():
        return int(card)
    else:
        return {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[card]

with open('input/day07.txt') as f:
    hands_and_bids = []
    for line in (l.rstrip("\n") for l in f.readlines()):
        hand, bid = line.split()
        hands_and_bids.append((tuple(card_to_num(card) for card in hand), int(bid)))

def strength(hand):
    return sorted(Counter(hand).values(), reverse=True)

hands_and_bids.sort(key = lambda e: (strength(e[0]), e[0])) # sort first by the strength of the hand type, then by the values in the hand itself
part1 = sum(bid*(i+1) for i, (hand, bid) in enumerate(hands_and_bids))

def replace_jokers(hand):
    hand_minus_jokers = tuple(card for card in hand if card!=11)
    if hand_minus_jokers: # if there's anything left after removing jokers, find the most common card and replace jokers with that
        best_hand = tuple(card if card!=11 else Counter(hand_minus_jokers).most_common(1)[0][0] for card in hand)
    else: # if all cards were jokers, it's already a five of a kind, so don't change it
        best_hand = hand
    individual_scores = tuple(card if card!=11 else 1 for card in hand)
    return strength(best_hand), individual_scores

hands_and_bids.sort(key=lambda e: replace_jokers(e[0]))
part2 = sum(bid*(i+1) for i, (hand, bid) in enumerate(hands_and_bids))

print(part1)
print(part2)