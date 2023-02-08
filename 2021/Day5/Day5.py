import numpy as np

with open("input.txt", "r") as f:
    vents_data = f.readlines()

vents_data = [line.replace('\n', '').split('->') for line in vents_data]
vents_data = [[line[0].split(','), line[1].split(',')] for line in vents_data]
vents_array = np.array(vents_data).astype('int16')
vents_max = vents_array.max() + 1
navigation_map = np.zeros(shape=(vents_max, vents_max), dtype='int16')
points_to_mark = []

for coord in vents_array:
    if coord[0, 0] == coord[1, 0]:
        if coord[0, 1] < coord[1, 1]:
            a = coord[0, 1]
            b = coord[1, 1]
        else:
            b = coord[0, 1]
            a = coord[1, 1]
        for i in range(a, b+1):
            navigation_map[i, coord[0, 0]] = navigation_map[i, coord[0, 0]] + 1
    elif coord[0, 1] == coord[1, 1]:
        if coord[0, 0] < coord[1, 0]:
            a = coord[0, 0]
            b = coord[1, 0]
        else:
            b = coord[0, 0]
            a = coord[1, 0]
        for i in range(a, b+1):
            navigation_map[coord[0, 1], i] = navigation_map[coord[0, 1], i] + 1

overlaps = np.sum(navigation_map > 1)
print(overlaps)
