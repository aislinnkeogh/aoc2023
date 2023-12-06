#!/usr/bin/env python

import numpy as np

with open('input/day06.txt') as f:
    for line in (l.rstrip("\n") for l in f.readlines()):
        if line.startswith("Time"):
            times = [int(x) for x in line.split(":")[1].split()]
        else:
            dists = [int(x) for x in line.split(":")[1].split()]

ways_to_win = []
for i, time in enumerate(times):
    for j in range(time):
        dist = (time-j) * j
        if dist > dists[i]:
            ways_to_win.append(len(range(j, time-j+1)))
            break

part1 = np.prod(ways_to_win)

time = int("".join([str(t) for t in times]))
dist = int("".join([str(d) for d in dists]))
for i in range(time):
    d = (time-i) * i
    if d > dist:
        part2 = len(range(i, time-i+1))
        break

print(part1)
print(part2)