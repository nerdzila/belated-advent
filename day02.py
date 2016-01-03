# -*- coding: utf-8 -*-
from advent_tools import get_input_string
from itertools import combinations
from functools import reduce
from operator import mul


input_string = get_input_string()

total_area, ribbon_length = (0, 0)
for line in input_string.split('\n'):
    dimensions = list(map(int, line.strip().split('x')))
    rectangle_sides = list(combinations(dimensions, 2))
    rectangle_areas = [x*y for x, y in rectangle_sides]
    slack = min(rectangle_areas)

    total_area += sum(2*area for area in rectangle_areas)
    total_area += slack

    perimeters = [2*x + 2*y for x, y in rectangle_sides]
    ribbon_length += min(perimeters)
    ribbon_length += reduce(mul, dimensions)

print(total_area)
print(ribbon_length)
