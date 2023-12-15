#!/usr/bin/env python

with open("input/day15.txt") as f:
    sequence = f.readlines()[0].rstrip("\n").split(",")

def HASH(step):
    val = 0
    for char in step:
        val = ((val + ord(char)) * 17) % 256
    return val

part1 = sum([HASH(step) for step in sequence])

lenses = [(step[:-2], int(step[-1])) if step[-2]=="=" else (step[:-1], 0) for step in sequence]

boxes = {i: [[],[]] for i in range(256)}
for lens in lenses:
    labels, focal_lengths = boxes[HASH(lens[0])]
    if lens[1] == 0:
        try:
            idx = labels.index(lens[0])
            labels.pop(idx)
            focal_lengths.pop(idx)
        except:
            pass
    else:
        try:
            idx = labels.index(lens[0])
            focal_lengths[idx] = lens[1]
        except:
            labels.append(lens[0])
            focal_lengths.append(lens[1])

part2 = 0
for i, box in boxes.items():
    for j, val in enumerate(box[1]):
        part2 += (i+1) * (j+1) * val

print(part1)
print(part2)