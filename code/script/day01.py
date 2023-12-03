#!/usr/bin/env python

import re

with open('input/day01.txt') as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

part1 = 0
for line in lines:
    digits = []
    for char in line:
        if char.isnumeric():
            digits.append(char)
    first_and_last = [digits[0], digits[-1]]
    part1 += int("".join(first_and_last))

regex_lines = []
for line in lines:
    line = re.sub("one", "o1e", line)
    line = re.sub("two", "t2o", line)
    line = re.sub("three", "t3e", line)
    line = re.sub("four", "4", line)
    line = re.sub("five", "5e", line)
    line = re.sub("six", "6", line)
    line = re.sub("seven", "7n", line)
    line = re.sub("eight", "e8t", line)
    line = re.sub("nine", "n9e", line)
    regex_lines.append(line)

part2 = 0
for line in regex_lines:
    digits = []
    for char in line:
        if char.isnumeric():
            digits.append(char)
    first_and_last = [digits[0], digits[-1]]
    part2 += int("".join(first_and_last))

print(part1)
print(part2)

with open('answers/day01.txt', 'w') as f:
    f.write(str(part1))
    f.write("\n")
    f.write(str(part2))