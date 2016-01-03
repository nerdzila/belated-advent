# -*- coding: utf-8 -*-
import inspect


def get_input_string():
    caller_frame = inspect.currentframe().f_back
    caller_file = caller_frame.f_locals['__file__']

    path_to_input = caller_file.replace('.py', '.in')

    with open(path_to_input, 'r') as input_file:
        raw_string = input_file.read()
        return raw_string.strip('\n')
