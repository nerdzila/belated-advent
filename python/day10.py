# -*- coding: utf-8 -*-
from advent_tools import print_answer

puzzle_input = input('Puzzle input: ')


def transform(line):
    line += '*'
    last_cut = 0
    sequences = []
    for offset, left, right in zip(range(1, len(line)), line[:-1], line[1:]):
        if left != right:
            sequences.append(line[last_cut:offset])
            last_cut = offset

    result = ''
    for seq in sequences:
        result += str(len(seq))
        result += seq[0]
    return result

for _ in range(40):
    puzzle_input = transform(puzzle_input)

print_answer(1, len(puzzle_input))

for _ in range(10):
    puzzle_input = transform(puzzle_input)

print_answer(2, len(puzzle_input))
