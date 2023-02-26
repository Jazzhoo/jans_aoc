
X = 0
Y = 0
trees=0
tree_map = []

with open("Input.txt", "r") as map_input:
    tree_map = map_input.readlines()

tree_map = [line[:-1] for line in tree_map]

for i, line in enumerate(tree_map):
    if X + 3 < len(line):
        X += 3
    else:
        X = (X + 3) - len(line)
    Y += 1
    if Y >= len(tree_map):
        continue
    if tree_map[Y][X] == "#":
        trees += 1
        temp_line = tree_map[i+1][:X] + "X" + tree_map[i+1][X+1:]
    else:
        temp_line = tree_map[i+1][:X] + "O" + tree_map[i+1][X+1:]

print(f"Trees approached: {trees}")
