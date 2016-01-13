# -*- coding: utf-8 -*-
import re
from advent_tools import print_answer

FORBIDDEN_LETTERS = re.compile('l|i|o')
CODEPOINT_START = ord('a')
CODEPOINT_LIMIT = ord('z')


def contains_straight(string):
    if len(string) < 3:
        return False

    triads = zip(string[:-2], string[1:-1], string[2:])
    return any((ord(f) + 2 == ord(s) + 1 == ord(t)) for f, s, t in triads)


def contains_two_pairs(string):
    if len(string) < 2:
        return False

    pairs = zip(string[:-1], string[1:])
    matching = set((left, right) for left, right in pairs if left == right)

    return len(matching) >= 2


def contains_forbidden_letters(string):
    return FORBIDDEN_LETTERS.match(string)


def is_valid_password(string):
    return (contains_straight(string)
            and contains_two_pairs(string)
            and not contains_forbidden_letters(string))


def increment_password(string):
    stop_increments = False
    inverted_result = ''

    for char in string[::-1]:
        if stop_increments:
            inverted_result += char
        else:
            next_codepoint = ord(char) + 1
            if next_codepoint > CODEPOINT_LIMIT:
                inverted_result += chr(CODEPOINT_START)
            else:
                inverted_result += chr(next_codepoint)
                stop_increments = True
    return inverted_result[::-1]


password = input('Password: ')
while not is_valid_password(password):
    password = increment_password(password)

print_answer(1, password)

password = increment_password(password)
while not is_valid_password(password):
    password = increment_password(password)

print_answer(2, password)
