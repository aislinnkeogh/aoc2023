#!/usr/bin/env python

import re

with open('input/day01.txt') as f:
    lines = [line.rstrip("\n") for line in f.readlines()]
    
parsed_lines = []
for old_line in lines:
    new_line = re.sub("one", "o1e", old_line)
    new_line = re.sub("two", "t2o", new_line)
    new_line = re.sub("three", "t3e", new_line)
    new_line = re.sub("four", "4", new_line)
    new_line = re.sub("five", "5e", new_line)
    new_line = re.sub("six", "6", new_line)
    new_line = re.sub("seven", "7n", new_line)
    new_line = re.sub("eight", "e8t", new_line)
    new_line = re.sub("nine", "n9e", new_line)
    parsed_lines.append((old_line, new_line))

def first_and_last_digit(str):
    return int("".join([re.search(r'\d', str).group(), re.search(r'\d', str[::-1]).group()]))

part1 = part2 = 0
for line in parsed_lines:
    part1 += first_and_last_digit(line[0])
    part2 += first_and_last_digit(line[1])

print(part1)
print(part2)