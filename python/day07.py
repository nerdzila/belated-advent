# -*- coding: utf-8 -*-
import inspect
from ctypes import c_uint16
from advent_tools import get_input_string, print_answer


class Input:
    def __init__(self, sources, operator):
        self.operator = operator
        self.sources = []

        for source in sources:
            try:
                source = int(source)
            except:
                pass
            self.sources.append(source)

    def __repr__(self):
        try:
            op = inspect.getsource(self.operator)
        except:
            op = 'None'

        return 'Input({!r}, {})'.format(self.sources, op)


def parse_input_spec(tokens):
    if len(tokens) == 1:
        return Input(sources=[tokens[0]], operator=None)

    if len(tokens) == 2:
        return Input(sources=[tokens[1]], operator=lambda x: ~x)

    if tokens[1] == 'AND':
        return Input(sources=tokens[::2], operator=lambda x, y: x & y)

    if tokens[1] == 'OR':
        return Input(sources=tokens[::2], operator=lambda x, y: x | y)

    shift = int(tokens[2])
    if tokens[1] == 'LSHIFT':
        return Input(sources=[tokens[0]], operator=lambda x: x << shift)

    return Input(sources=[tokens[0]], operator=lambda x: x >> shift)


inputs = {}
for line in get_input_string().split('\n'):
    tokens = line.split()
    parsed = parse_input_spec(tokens[:-2])
    inputs[tokens[-1]] = parsed

results = {}


def solve(key):
    input_ = inputs[key]

    args = []
    for source in input_.sources:
        if isinstance(source, int):
            args.append(source)
        else:
            if source not in results:
                solve(source)
            args.append(results[source])

    if input_.operator is None:
        results[key] = args[0]
    else:
        results[key] = input_.operator(*args)

solve('a')
first_answer = c_uint16(results['a']).value
print_answer(1, first_answer)

inputs['b'] = Input(sources=[first_answer], operator=None)
results = {}
solve('a')
second_answer = c_uint16(results['a']).value

print_answer(2, second_answer)
