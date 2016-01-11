# -*- coding: utf-8 -*-
from math import inf
from itertools import permutations
from advent_tools import get_input_lines, print_answer


distances = dict()
places = set()
for line in get_input_lines():
    left, _, right, _, distance = line.split()
    distance = int(distance)

    places.add(left)
    places.add(right)
    distances[frozenset((left, right))] = distance

shortest_length = inf
shortest_route = None
biggest_length = 0
longest_route = None

for route in permutations(places):
    route_length = 0
    trips = zip(route[:-1], route[1:])
    route_length = sum(distances[frozenset(t)] for t in trips)
    if route_length < shortest_length:
        shortest_length = route_length
        shortest_route = route

    if route_length > biggest_length:
        biggest_length = route_length
        longest_route = route

print_answer(1, shortest_length)

print_answer(2, biggest_length)
