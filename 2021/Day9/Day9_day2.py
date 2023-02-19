import numpy as np
from helper_function import helper_functions as hf

with open("input_files/example_input.txt", "r") as f:
#with open("input_files/input.txt", "r") as f:
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
    pass


for i, lowest_point in enumerate(lowest_points):
    score = traverse_basin(heightmap_array, lowest_point)
