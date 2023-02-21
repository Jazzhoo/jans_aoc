import numpy as np

# with open("input_files/example_input.txt", "r") as f:
with open("input_files/input.txt", "r") as f:
        nav_system_raw = f.readlines()

nav_system = [[char for char in line.strip()] for line in nav_system_raw]
score_match = {')': ('(', 3), ']': ('[', 57), '}': ('{', 1197), '>': ('<', 25137)}
score_total = 0

OPENING_BR = ['(', '[', '{', '<']
CLOSING_BR = score_match.keys()

for line in nav_system:
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
                break

print(f'Total score is: {score_total}')

