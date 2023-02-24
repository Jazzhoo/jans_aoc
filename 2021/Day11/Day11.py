import numpy as np

# with open("input_files/example_input.txt", "r") as f:
with open("input_files/input.txt", "r") as f:
        nav_system_raw = f.readlines()

nav_system = [[char for char in line.strip()] for line in nav_system_raw]
score_match = {')': ('(', 3), ']': ('[', 57), '}': ('{', 1197), '>': ('<', 25137)}
score_total = 0
discard_indexes = []

OPENING_BR = ['(', '[', '{', '<']
CLOSING_BR = score_match.keys()


for i, line in enumerate(nav_system):
    line_check = []
    for char in line:
        if char in OPENING_BR:
            line_check.append(char)
        elif char in CLOSING_BR:
            if score_match[char][0] == line_check[-1]:
                line_check.pop()
                continue
            else:
                score_total += score_match[char][1]
                discard_indexes.append(i)
                break

print(f'Total score is: {score_total}')


# part 2
discard_indexes.sort(reverse=True)

for idx in discard_indexes:
    nav_system.pop(idx)

line_closers = {'(': (')', 1), '[': (']', 2), '{': ('}', 3), '<': ('>', 4)}
#score_total = 0
score_list = []
pass

for i, line in enumerate(nav_system):
    line_check = []
    for char in line:
        if char in OPENING_BR:
            line_check.append(char)
        elif char in CLOSING_BR:
            if score_match[char][0] == line_check[-1]:
                line_check.pop()
                continue

    score_total = 0
    while line_check:
        char = line_check.pop()
        line.append(line_closers[char][0])
        score_total *= 5
        score_total += line_closers[char][1]

    score_list.append(score_total)

score_list.sort()
middle_idx = (len(score_list) - 1) / 2
score_total = score_list[int(middle_idx)]

print(f"Part 2 total score: {score_total}")
