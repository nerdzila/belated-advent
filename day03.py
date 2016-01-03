# -*- coding: utf-8 -*-
from advent_tools import get_input_string

shifts = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0)
}


def move(current_pos, direction):
    shift = shifts[direction]
    return (current_pos[0] + shift[0], current_pos[1] + shift[1])

instructions = get_input_string()

position = (0, 0)
visited = {position}

for direction in instructions:
    position = move(position, direction)
    visited.add(position)

print('Houses visited during 1st year: {}'.format(len(visited)))

santa = (0, 0)
robo_santa = (0, 0)

visited = {(0, 0)}

for idx, direction in enumerate(instructions):
    if idx % 2 == 0:
        santa = move(santa, direction)
        visited.add(santa)
    else:
        robo_santa = move(robo_santa, direction)
        visited.add(robo_santa)

print('Houses visited during 2nd year: {}'.format(len(visited)))
