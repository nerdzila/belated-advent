# -*- coding: utf-8 -*-
from itertools import combinations
from functools import reduce
from operator import mul
from advent_tools import get_input_lines, print_answer


total_area, ribbon_length = (0, 0)
for line in get_input_lines():
    dimensions = list(map(int, line.strip().split('x')))
    rectangle_sides = list(combinations(dimensions, 2))
    rectangle_areas = [x*y for x, y in rectangle_sides]
    slack = min(rectangle_areas)

    total_area += sum(2*area for area in rectangle_areas)
    total_area += slack

    perimeters = [2*x + 2*y for x, y in rectangle_sides]
    ribbon_length += min(perimeters)
    ribbon_length += reduce(mul, dimensions)

print_answer(1, total_area)
print_answer(2, ribbon_length)
