# -*- coding: utf-8 -*-
from collections import defaultdict
from itertools import permutations
from math import inf
from advent_tools import get_input_lines, print_answer


def compute_change(guests, happiness_score):
    biggest_change = -inf
    for perm in permutations(guests):
        seatings = list(perm) + [perm[0]]
        pairings = zip(seatings[:-1], seatings[1:])

        change = 0
        for l, r in pairings:
            change += happiness_score[l][r]
            change += happiness_score[r][l]

        if change > biggest_change:
            biggest_change = change

    return biggest_change


happiness_score = defaultdict(dict)

for line in get_input_lines():
    tokens = line.rstrip('.').split()
    left, _, effect, amount = tokens[:4]
    right = tokens[-1]

    score = int(amount) if effect == 'gain' else -int(amount)

    happiness_score[left][right] = score

guests = list(happiness_score.keys())

print_answer(1, compute_change(guests, happiness_score))

for key in list(happiness_score.keys()):
    happiness_score[key]['nerdzila'] = 0
    happiness_score['nerdzila'][key] = 0

guests.append('nerdzila')

print_answer(2, compute_change(guests, happiness_score))
