import numpy as np

with open("input_files/input.txt", "r") as f:
#with open("input_files/example_input.txt", "r") as f:
    octo_map = f.readlines()

octo_map = [[int(c) for c in line.strip()] for line in octo_map]
octo_array = np.array(octo_map)
flash_counter = 0


def flash_octo(octo: tuple[int, int], array: np.ndarray) -> list[tuple[int, int]]:
    moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    row, col = octo
    array[row, col] = 0
    _ROW_MAX, _COL_MAX = array.shape
    _newly_loaded_octos = []
    for move in moves:
        nrow = row + move[0]
        ncol = col + move[1]

        if nrow < 0 or nrow > _ROW_MAX - 1:
            continue
        elif ncol < 0 or ncol > _COL_MAX - 1:
            continue
        elif array[nrow, ncol] == 0 or array[nrow, ncol] > 9:
            continue
        else:
            array[nrow, ncol] += 1
            if array[nrow, ncol] > 9:
                _newly_loaded_octos.append((nrow, ncol))

    return _newly_loaded_octos

i = 0

while True:
    i += 1
    octo_array += 1
    x = np.where(octo_array > 9)
    loaded_octo_list = set()
    for t in range(len(x[0])):
        loaded_octo_list.add((x[0][t], x[1][t]))
    local_flash_counter = 0

    while loaded_octo_list:
        loaded_octo = loaded_octo_list.pop()
        newly_loaded_octos = flash_octo(loaded_octo, octo_array)
        loaded_octo_list.symmetric_difference_update(newly_loaded_octos)
        flash_counter += 1
        local_flash_counter += 1
        pass
    if local_flash_counter == 100:
        print(f"All octos flash on step {i}")
        break
    pass


print(f"{flash_counter} flashes occured")


