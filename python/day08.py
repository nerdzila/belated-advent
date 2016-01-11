# -*- coding: utf-8 -*-
import re
from advent_tools import get_input_lines, print_answer

decode_pattern = re.compile(r'(\\\\)|(\\\")|(\\x[0-9a-f]{2})')
encoding_subs = [
    (re.compile(r'\\'), r'\\\\'),
    (re.compile(r'\"'), r'\\"')
]

total_code_chars = 0
total_memory_size = 0
total_encoded_size = 0

for line in get_input_lines():
    meaty_part = line[1:-1]
    mem_length = len(decode_pattern.sub('?', meaty_part))
    total_code_chars += len(line)
    total_memory_size += mem_length

    encoded_line = line
    for pattern, sub in encoding_subs:
        encoded_line = pattern.sub(sub, encoded_line)

    encoded_line = '"{}"'.format(encoded_line)
    total_encoded_size += len(encoded_line)


print_answer(1, total_code_chars - total_memory_size)
print_answer(2, total_encoded_size - total_code_chars)
