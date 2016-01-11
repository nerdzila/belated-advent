# -*- coding: utf-8 -*-
import hashlib
from advent_tools import print_answer

ENCODING = 'utf-8'


def hash_key_and_number(key, number):
    m = hashlib.md5()
    m.update(key.encode(ENCODING))
    m.update(str(number).encode(ENCODING))
    return m.hexdigest()


def find_hash_seed(prefix, key):
    current_number = 0

    while True:
        current_number += 1
        current_hash = hash_key_and_number(puzzle_input, current_number)
        if current_hash.startswith(prefix):
            return current_number

puzzle_input = input('Puzzle key: ')


print_answer(1, find_hash_seed('00000', puzzle_input))
print_answer(2, find_hash_seed('000000', puzzle_input))
