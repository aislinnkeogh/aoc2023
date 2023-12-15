#!/usr/bin/env python

import numpy as np
from collections import defaultdict

with open("input/day15.txt") as f:
    sequence = f.readlines()[0].rstrip("\n").split(",")

def HASH(step):
    val = 0
    for char in step:
        val = ((val + ord(char)) * 17) % 256
    return val

part1 = sum([HASH(step) for step in sequence])

lenses = [(step[:-2], int(step[-1])) if step[-2]=="=" else (step[:-1], 0) for step in sequence]

def default_val(): 
    return ([], [])

boxes = defaultdict(default_val)
for step in lenses:
    labels, focal_lengths = boxes[HASH(step[0])]
    if step[1] == 0:
        try:
            idx = labels.index(step[0])
            labels.pop(idx)
            focal_lengths.pop(idx)
        except:
            pass
    else:
        try:
            idx = labels.index(step[0])
            focal_lengths[idx] = step[1]
        except:
            labels.append(step[0])
            focal_lengths.append(step[1])

part2 = 0
for i in boxes.keys():
    for j in range(len(boxes[i][1])):
        part2 += np.prod([i+1, j+1, boxes[i][1][j]])

print(part1)
print(part2)