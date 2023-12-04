#!/usr/bin/env python

with open('input/day04.txt') as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

cards = {i+1: {"winning": lines[i].split(": ")[1].split(" | ")[0].split(), "have": lines[i].split(": ")[1].split(" | ")[1].split()} for i in range(len(lines))}
matches = [len([e for e in cards[i+1]["winning"] if e in cards[i+1]["have"]]) for i in range(len(cards))]
part1 = sum([2**(m-1) for m in matches if m>0])

copies = {c: 1 for c in cards}
for i in range(len(cards)):
    for j in range(matches[i]):
        copies[i+j+2] += copies[i+1]
part2 = sum(copies.values())

print(part1)
print(part2)