import numpy as np

with open("input.txt", "r") as f:
    game_tactics = f.readlines()

game_tactics = [x.strip().split(' ') for x in game_tactics]
game_rules = np.zeros(shape=[4, 3], dtype=np.int8)
game_dict = {"A": 1, "X": 0, "B": 2, "Y": 3, "C": 3, "Z": 6}

game_rules[1, 0] = 3
game_rules[2, 0] = 1
game_rules[3, 0] = 2
game_rules[1, 1] = 1
game_rules[2, 1] = 2
game_rules[3, 1] = 3
game_rules[1, 2] = 2
game_rules[2, 2] = 3
game_rules[3, 2] = 1

result = 0
for line in game_tactics:
    result += game_dict[line[1]] + game_rules[game_dict[line[0]], int(game_dict[line[1]]/3)]

print(f"final result is: {result}")



ffdgjogjdjgfdkgsdkgjdfklgjkdjfkhjfgkhjkldfjgldfjkhjkdfjgkdjfkhjkldfjgklsjlkdfkgjdfkhkdfgdfkgjkdfjgfdgjogjdjgfdkgsdkgjdfklgjkdjfkhjfgkhjkldfjgldfjkhjkdfjgkdjfkhjkldfjgklsjlkdfkgjdfkhkdfgdfkgjkdfjgfdgjogjdjgfdkgsdkgjdfklgjkdjfkhjfgkhjkldfjgldfjkhjkdfjgkdjfkhjkldfjgklsjlkdfkgjdfkhkdfgdfkgjkdfjgfdgjogjdjgfdkgsdkgjdfklgjkdjfkhjfgkhjkldfjgldfjkhjkdfjgkdjfkhjkldfjgklsjlkdfkgjdfkhkdfgdfkgjkdfjgfdgjogjdjgfdkgsdkgjdfklgjkdjfkhjfgkhjkldfjgldfjkhjkdfjgkdjfkhjkldfjgklsjlkdfkgjdfkhkdfgdfkgjkdfjgfdgjogjdjgfdkgsdkgjdfklgjkdjfkhjfgkhjkldfjgldfjkhjkdfjgkdjfkhjkldfjgklsjlkdfkgjdfkhkdfgdfkgjkdfjgdgjogjdjgfdkgsdkgjdfklgjkdjfkhjfgkhjkldfjgldfjkhjkdfjgkdjfkhjkldfjgklsjlkdfkgjdfkhkdfgdfkgjkdfjg