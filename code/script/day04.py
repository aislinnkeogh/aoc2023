#!/usr/bin/env python

with open('input/day04.txt') as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

cards = {i+1: {"winning": line.split(": ")[1].split(" | ")[0].split(), "have": line.split(": ")[1].split(" | ")[1].split()} for i, line in enumerate(lines)}
matches = [len(set(cards[i+1]["winning"]).intersection(set(cards[i+1]["have"]))) for i in range(len(cards))]
part1 = sum([2**(m-1) for m in matches if m>0])

copies = {c: 1 for c in cards}
for i in range(len(cards)):
    for j in range(matches[i]):
        copies[i+j+2] += copies[i+1]
part2 = sum(copies.values())

print(part1)
print(part2)