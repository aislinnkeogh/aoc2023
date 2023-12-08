#!/usr/bin/env python

import numpy as np

with open("input/day08.txt") as f:
    lines = [line for line in (l.rstrip("\n") for l in f.readlines())]

directions = [{"L": 0, "R": 1}[letter] for letter in lines[0]]
nodes = lines[2:]

node_lookup = {}
for node in nodes:
    start, options = node.split(" = ")
    node_lookup[start] = tuple(options.strip("()").split(", "))

# Part 1
keep_going = True
next_key = "AAA"
part1 = 0
while keep_going:
    for i in directions:
        next_key = node_lookup[next_key][i]
        part1 += 1
        if next_key == "ZZZ":
            keep_going = False

# Part 2
starting_keys = [key for key in node_lookup.keys() if key.endswith("A")]
steps_per_starting_key = []
for key in starting_keys:
    keep_going = True
    next_key = key
    n_steps = 0
    while keep_going:
        for i in directions:
            next_key = node_lookup[next_key][i]
            n_steps += 1
            if next_key.endswith("Z"):
                steps_per_starting_key.append(n_steps)
                keep_going = False

part2 = np.lcm.reduce(steps_per_starting_key)

print(part1)
print(part2)