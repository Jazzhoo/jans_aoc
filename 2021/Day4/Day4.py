import numpy as np


def check_board(input):
    axis0 = np.sum(input, axis=0)
    axis1 = np.sum(input, axis=1)
    res_axis0 = np.where(axis0==5)
    res_axis1 = np.where(axis1==5)
    if len(res_axis0[0]):
        rev_input = 1 - input
        unmarked_board = table * rev_input
        temp_result = np.sum(unmarked_board)
        return True, temp_result
    if len(res_axis1[0]):
        rev_input = 1 - input
        unmarked_board = table * rev_input
        temp_result = np.sum(unmarked_board)
        return True, temp_result
    return False, 0


with open("input.txt", "r") as f:
    bingo_input = f.readlines()

chosen_numbers = bingo_input.pop(0)
chosen_numbers = chosen_numbers.split(',')
chosen_numbers = [int(a) for a in chosen_numbers]

list_of_boards = []
for i in range(int(len(bingo_input)/6)):
    list_of_boards.append(np.loadtxt(bingo_input[6*i:6*(i+1)], dtype=np.int8))

list_of_results = [np.zeros(shape=(5, 5), dtype=np.int8) for _ in list_of_boards]

for num in chosen_numbers:
    breakFlag = False
    for idx, table in enumerate(list_of_boards):
        res = np.where(table == num)
        if len(res[0]):
            list_of_results[idx][res[0][0]][res[1][0]] = 1
            check = check_board(list_of_results[idx])
            if check[0]:
                print(check[1] * num)
                breakFlag = True
                break
    if breakFlag:
        break

