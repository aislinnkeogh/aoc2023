#!/usr/bin/env python

import re
import numpy as np

with open('input/day03.txt') as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

def check_for_symbols(grid, x, y):
    
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
            try:
                if re.match(r"[^\d.]", grid[i][j]):
                    return True
            except:
                pass
        
    return False

positions_adjacent_to_symbols = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if check_for_symbols(lines, i, j):
            positions_adjacent_to_symbols.append((i, j))

numbers = []
spans = []
for i in range(len(lines)):
    for match in re.finditer(r"(\d+)", lines[i]):
        numbers.append(match.group())
        spans.append([(i, j) for j in range(match.span()[0], match.span()[1])])

part1 = 0
for i in range(len(numbers)):
    if [e for e in spans[i] if e in positions_adjacent_to_symbols]:
        part1 += int(numbers[i])

def check_for_gears(grid, x, y):
    
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
            try:
                if grid[i][j] == "*":
                    return (i, j)
            except:
                pass
        
    return False

potential_gears = {}
for i in range(len(spans)):
    for pos in spans[i]:
        gear_position = check_for_gears(lines, pos[0], pos[1])
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
        part2 += np.prod(potential_gears[gear])

print(part1)
print(part2)