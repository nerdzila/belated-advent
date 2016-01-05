# -*- coding: utf-8 -*-
import inspect
from os import path


def get_input_string():
    caller_frame = inspect.currentframe().f_back
    caller_file = caller_frame.f_locals['__file__']

    input_file = path.basename(caller_file).replace('.py', '.in')

    cd = path.abspath(path.dirname(caller_file) + '/../input')
    path_to_input = path.join(cd, input_file)

    with open(path_to_input, 'r') as input_file:
        raw_string = input_file.read()
        return raw_string.strip('\n')


def print_answer(which_answer, answer):
    print('Answer #{}: {}'.format(which_answer, answer))
