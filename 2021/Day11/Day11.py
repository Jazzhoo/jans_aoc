import numpy as np

# with open("input_files/example_input.txt", "r") as f:
with open("input_files/example_input.txt", "r") as f:
    octo_map = f.readlines()

octo_map = [[int(c) for c in line.strip()] for line in octo_map]
octo_array = np.array(octo_map)
flash_counter = 0

for i in range(100):
    octo_array += 1
    x = np.where(octo_array > 9)
    loaded_octo_list = []
    for t in range(len(x[0])):
        loaded_octo_list.append((x[0][t], x[1][t]))

    while loaded_octo_list:
        loaded_octo = loaded_octo_list.pop(0)
        pass
    pass


