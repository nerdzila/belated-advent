# -*- coding: utf-8 -*-
import array
from advent_tools import get_input_string, print_answer


class BinaryGrid:
    def __init__(self, width, height, start_value=1):
        self.width = width
        self.height = height
        self.size = width * height
        self.grid = array.array('B', [start_value] * self.size)

    def update(self, x_pos, y_pos, update_cb):
        idx = x_pos * self.width + y_pos
        self.grid[idx] = update_cb(self.grid[idx])


class Instruction:
    CALLBACKS = {
        'turn on': (lambda x: 1),
        'turn off': (lambda x: 0),
        'toggle': (lambda x: not x)
    }

    def __init__(self, instruction_string):
        tokens = instruction_string.split()

        self.x_end, self.y_end = map(int, tokens[-1].split(','))
        self.x_start, self.y_start = map(int, tokens[-3].split(','))
        self.command = self.CALLBACKS[' '.join(tokens[:-3])]

    def x_range(self):
        return range(self.x_start, self.x_end + 1)

    def y_range(self):
        return range(self.y_start, self.y_end + 1)


class UpdatedInstruction(Instruction):
    CALLBACKS = {
        'turn on': (lambda x: x + 1),
        'turn off': (lambda x: 0 if x - 1 < 0 else x - 1),
        'toggle': (lambda x: x + 2)
    }


g1 = BinaryGrid(1000, 1000, 0)
g2 = BinaryGrid(1000, 1000, 0)


for line in get_input_string().split('\n'):
    print(line)
    first = Instruction(line)
    second = UpdatedInstruction(line)

    for x in first.x_range():
        for y in second.y_range():
            g1.update(x, y, first.command)
            g2.update(x, y, second.command)

print_answer(1, sum(g1.grid))
print_answer(2, sum(g2.grid))
