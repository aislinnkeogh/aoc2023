#!/usr/bin/env python

with open("input/day09.txt") as f:
    histories = [[int(val) for val in line.split()] for line in (l.rstrip("\n") for l in f.readlines())]

part1 = 0
part2 = 0
for h in histories:
    diffs = [h]
    keep_going = True
    while keep_going:
        # diffs.append([diffs[-1][i+1]-diffs[-1][i] for i in range(len(diffs[-1])-1)])
        diffs.append([diffs[-1][i+1]-val for i, val in enumerate(diffs[-1][:-1])])
        if set(diffs[-1]) == {0}:
            for j in range(len(diffs)-1, 0, -1):
                diffs[j-1].append(diffs[j-1][-1] + diffs[j][-1])
                diffs[j-1].insert(0, diffs[j-1][0] - diffs[j][0])
            part1 += diffs[0][-1]
            part2 += diffs[0][0]
            keep_going = False

print(part1)
print(part2)