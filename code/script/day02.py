#!/usr/bin/env python

from functools import reduce

with open('input/day02.txt') as f:
    games = [[rnd.split(", ") for rnd in game] for game in [line.rstrip("\n").split(": ")[1].split("; ") for line in f.readlines()]]

highest_per_game = {i: {"red": 0, "green": 0, "blue": 0} for i in range(len(games))}
for i, game in enumerate(games):
    for rnd in game:
        for clr in rnd:
            n, x = clr.split(" ")
            if int(n) > highest_per_game[i][x]:
                highest_per_game[i][x] = int(n)

part1 = 0
part2 = 0
for i, v in highest_per_game.items():
    if v["red"] <= 12 and v["green"] <= 13 and v["blue"] <= 14:
        part1 += i+1
    part2 += reduce((lambda x, y: x * y), v.values())

print(part1)
print(part2)