# -*- coding: utf-8 -*-
import inspect
from os import path


def get_input_file_path():
    caller_frame = inspect.currentframe().f_back.f_back
    caller_file = caller_frame.f_locals['__file__']

    input_file = path.basename(caller_file).replace('.py', '.in')

    cd = path.abspath(path.dirname(caller_file) + '/../input')
    return path.join(cd, input_file)


def get_input_string():
    with open(get_input_file_path(), 'r') as input_file:
        raw_string = input_file.read()
        return raw_string.strip('\n')


def get_input_lines():
    with open(get_input_file_path(), 'r') as input_file:
        for line in input_file:
            yield line.strip()


def print_answer(which_answer, answer):
    print('Answer #{}: {}'.format(which_answer, answer))
