#!/usr/bin/env python

import re
from functools import reduce

with open('input/day03.txt') as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

def check_grid(grid, x, y, target):
    
    positions_to_check = [
        (x, y-1),
        (x, y+1),
        (x-1, y-1),
        (x-1, y),
        (x-1, y+1),
        (x+1, y-1),
        (x+1, y),
        (x+1, y+1)
    ]

    for i, j in positions_to_check:
        if i < 0 or j < 0:
            pass
        else:
            if target=="symbols":
                try:
                    if re.match(r"[^\d.]", grid[i][j]):
                        return True
                except:
                    pass
            elif target=="gears":
                try:
                    if grid[i][j] == "*":
                        return (i, j)
                except:
                    pass
            
    return False

numbers = []
spans = []
for i, line in enumerate(lines):
    for match in re.finditer(r"(\d+)", line):
        numbers.append(match.group())
        spans.append([(i, j) for j in range(match.span()[0], match.span()[1])])

part1 = 0
for i, n in enumerate(numbers):
    if [e for e in spans[i] if check_grid(lines, e[0], e[1], "symbols")]:
        part1 += int(n)

potential_gears = {}
for i, span in enumerate(spans):
    for pos in span:
        gear_position = check_grid(lines, pos[0], pos[1], "gears")
        if gear_position:
            try:
                potential_gears[gear_position].append(int(numbers[i]))
            except:
                potential_gears[gear_position] = [int(numbers[i])]
            finally:
                break

part2 = 0
for gear in potential_gears:
    if len(potential_gears[gear]) == 2:
        part2 += reduce((lambda x, y: x * y), potential_gears[gear])

print(part1)
print(part2)