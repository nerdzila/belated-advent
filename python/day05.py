# -*- coding: utf-8 -*-
from advent_tools import get_input_string, print_answer


class FirstNicenessEvaluator:
    NAUGHTY_STRINGS = {'ab', 'cd', 'pq', 'xy'}

    def __init__(self):
        self.vowel_count = 0
        self.letter_repeats = False
        self.naughty_strings = set()
        self.previous_char = ''

    def read(self, char):
        if char == self.previous_char:
            self.letter_repeats = True

        if (self.previous_char + char) in self.NAUGHTY_STRINGS:
            self.naughty_strings.add(self.previous_char + char)

        if char in 'aeiou':
            self.vowel_count += 1

        self.previous_char = char

    def is_nice(self):
        return (self.vowel_count >= 3
                and self.letter_repeats
                and len(self.naughty_strings) == 0)


class SecondNicenessEvaluator:
    def __init__(self):
        self.last = ''
        self.second_to_last = ''
        self.has_almost_contiguous_pair = False
        self.repeats_non_overlapping_pairs = False
        self.seen_pairs = set()

    def read(self, char):
        if char == self.second_to_last:
            self.has_almost_contiguous_pair = True

        if (self.last + char) in self.seen_pairs:
            self.repeats_non_overlapping_pairs = True

        previous_pair = self.second_to_last + self.last
        if len(previous_pair) == 2:
            self.seen_pairs.add(previous_pair)

        self.second_to_last = self.last
        self.last = char

    def is_nice(self):
        return (self.has_almost_contiguous_pair
                and self.repeats_non_overlapping_pairs)


def evaluate_words(evaluator, lines):
    nice_ones = 0
    for line in lines.split('\n'):
        ne = evaluator()

        for char in line:
            ne.read(char)

        if ne.is_nice():
            nice_ones += 1

    return nice_ones

input_string = get_input_string()


print_answer(1, evaluate_words(FirstNicenessEvaluator, input_string))
print_answer(2, evaluate_words(SecondNicenessEvaluator, input_string))
