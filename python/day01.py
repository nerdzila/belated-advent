# -*- coding: utf-8 -*-
from advent_tools import get_input_string, print_answer


def direction(instruction):
    if instruction == '(':
        return 1

    if instruction == ')':
        return -1

    raise ValueError('Instruction has to be either "(" or ")"')


input_string = get_input_string()

first_answer = input_string.count('(') - input_string.count(')')

print_answer(1, first_answer)

current_floor = 0

for idx, instruction in enumerate(input_string):
    current_floor += direction(instruction)

    if current_floor < 0:
        print_answer(2, idx + 1)
        break

if current_floor >= 0:
    print('Second answer: Negative floor was never reached')
