import numpy as np
from helper_function import helper_functions as hf

#with open("input_files/example_input.txt", "r") as f:
with open("input_files/input.txt", "r") as f:
        heightmap = f.readlines()

heightmap_array = []

for line in heightmap:
    heightmap_array.append([int(a) for a in line.strip()])
heightmap_array = np.array(heightmap_array)

shape = heightmap_array.shape
result = 0
lowest_points = {}

for x, row in enumerate(heightmap_array):
    for y, var in enumerate(row):
        ifis = hf.check_if_lowest(heightmap_array, x, y)
        if ifis:
            lowest_points[(x, y)] = var
            result += var + 1

print("The lowest points are: ", lowest_points)
print("Result is: ", result)

# starting part 2
visited_basins = []


def traverse_basin(heightmap_array, lowest_point):
    print(f"processing point: (row: {lowest_point[0]}, col: {lowest_point[1]})")
    _tracking_basin = []
    _result = 0
    _places_to_check = [lowest_point]
    _tracking_basin.append(lowest_point)

    while _places_to_check:
        _result += 1
        current_place = _places_to_check.pop()
        _places_to_check.extend(hf.traverse_deeper(heightmap_array, current_place, _tracking_basin))

    return _result


scores = []
for i, lowest_point in enumerate(lowest_points):
    scores.append(traverse_basin(heightmap_array, lowest_point))

scores.sort(reverse=True)
print(np.prod(scores[:3]))
