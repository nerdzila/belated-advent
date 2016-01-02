# -*- coding: utf-8 -*-


def direction(instruction):
    if instruction == '(':
        return 1

    if instruction == ')':
        return -1

    raise ValueError('Instruction has to be either "(" or ")"')

with open('day01.in') as input_file:
    input_string = input_file.read()

    first_answer = input_string.count('(') - input_string.count(')')

    print('First answer: {}'.format(first_answer))

    current_floor = 0

    for idx, instruction in enumerate(input_string):
        current_floor += direction(instruction)

        if current_floor < 0:
            print('Second answer: {}'.format(idx + 1))
            break

    if current_floor >= 0:
        print('Second answer: Negative floor was never reached')
