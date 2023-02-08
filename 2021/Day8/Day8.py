with open("input_files/input.txt", "r") as f:
    code_lines = f.readlines()

code_lines = [line.split('|') for line in code_lines]
output_digits = [line[1].strip().split(' ') for line in code_lines]
output = [x for y in output_digits for x in y if len(x) in [2, 3, 4, 7]]
print(f'occurances: {len(output)}')