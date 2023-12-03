#!/usr/bin/env python

import numpy as np

with open('input/day02.txt') as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

games = [line.split(": ")[1].split("; ") for line in lines]
parsed_games = [[rnd.split(", ") for rnd in game] for game in games]

all_games = {}
for i in range(len(parsed_games)):
    all_games[i+1] = []
    for j in range(len(parsed_games[i])):
        all_games[i+1].append({"red": 0, "green": 0, "blue": 0})
        for clr in parsed_games[i][j]:
            n, x = clr.split(" ")
            all_games[i+1][j][x] += int(n)

highest_per_game = {}
for i in range(len(all_games)):
    highest_per_game[i+1] = {"red": 0, "green": 0, "blue": 0}
    for rnd in all_games[i+1]:
        for clr in ["red", "green", "blue"]:
            if rnd[clr] > highest_per_game[i+1][clr]:
                highest_per_game[i+1][clr] = rnd[clr]

part1 = 0
for i in range(len(highest_per_game)):
    if highest_per_game[i+1]["red"] <= 12 and highest_per_game[i+1]["green"] <= 13 and highest_per_game[i+1]["blue"] <= 14:
        part1 += i+1

part2 = np.sum([np.prod(list(highest_per_game[i+1].values())) for i in range(len(highest_per_game))])

print(part1)
print(part2)