# -*- coding: utf-8 -*-
import re
import json
from advent_tools import get_input_string, print_answer

NUMBERS = re.compile('-?\d+')
input_string = get_input_string()

print_answer(1, sum(map(int, NUMBERS.findall(input_string))))

root = json.loads(input_string)


def explore(node, total):
    if isinstance(node, int):
        return total + node

    if isinstance(node, dict):
        if 'red' in node.values():
            return total

        acum = 0
        for n in node.values():
            acum += explore(n, 0)

        return total + acum

    if isinstance(node, list):
        acum = 0
        for n in node:
            acum += explore(n, 0)

        return total + acum

    return total

print_answer(2, explore(root, 0))
