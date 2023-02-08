import collections

with open("input_files/example_input.txt", "r") as f:
    heatmap = f.readlines()

coords = collections.defaultdict(lambda: 9)

for y, line in enumerate(heatmap):
    for x, c in enumerate(line):
        coords[(x, y)] = int(c)

