#!/usr/bin/env python

with open('input/day04.txt') as f:
    cards = []
    for i, line in enumerate(l.rstrip("\n") for l in f.readlines()):
        winning, have = line.split(": ")[1].split(" | ")
        cards.append((winning.split(), have.split()))

matches = [len(set(cards[i][0]).intersection(set(cards[i][1]))) for i in range(len(cards))]
part1 = sum([2**(m-1) for m in matches if m>0])

copies = {i+1: 1 for i in range(len(cards))}
for i in range(len(cards)):
    for j in range(matches[i]):
        copies[i+j+2] += copies[i+1]
part2 = sum(copies.values())

print(part1)
print(part2)