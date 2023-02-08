import numpy as np


def check_board(input):
    axis0 = np.sum(input, axis=0)
    axis1 = np.sum(input, axis=1)
    res_axis0 = np.where(axis0==5)
    res_axis1 = np.where(axis1==5)
    if res_axis0[0].size > 0:
        rev_input = 1 - input
        unmarked_board = table * rev_input
        temp_result = np.sum(unmarked_board)
        return True, temp_result
    if res_axis1[0].size > 0:
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

list_of_results = [np.zeros(shape=(5, 5), dtype=np.int8) for a in list_of_boards]
winning_scores = []
winning_boards = []
winning_results = []
for num in chosen_numbers:
    boards_to_remove = []
    for idx, table in enumerate(list_of_boards):
        res = np.where(table == num)
        if res[0].size > 0:
            list_of_results[idx][res[0][0], res[1][0]] = 1
            check = check_board(list_of_results[idx])
            if check[0]:
                winning_scores.append(check[1] * num)
                boards_to_remove.append(idx)
    boards_to_remove.sort(reverse=True)
    for board in boards_to_remove:
        del list_of_boards[board]
        del list_of_results[board]
print(winning_scores[-1])
