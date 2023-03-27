with open("input.txt", "r") as f:
    crates_with_instruction = f.readlines()

stack_count = 0
for line in crates_with_instruction:
    if any(a.isnumeric() for a in line):
        tmp_stack_count = [int(a) for a in line.replace(' ', '').strip()]
        stack_count = max(tmp_stack_count)
        break
crates = ["" for i in range(stack_count)]
instruction = []
breaking_line = 0

for line in crates_with_instruction:
    if line.removesuffix('\n') != "":
        lineLen = len(line)
        for chr in range(0, lineLen, 4):
            column = int(chr / 4)
            crate = ""
            if line[chr] == " ":
                continue
            else:
                crate = [a if a.isalpha() else '' for a in line[chr:chr+3]]
                crate = ''.join(crate)
                crates[column] += crate
            pass
    else:
        breaking_line = crates_with_instruction.index(line)
        break

for idx in range(len(crates)):
    crates[idx] = crates[idx][::-1]

for line in crates_with_instruction[breaking_line + 1:]:
    instruction.append(line.strip().split(' '))

instruction = [[int(line[1]), int(line[3]), int(line[5])] for line in instruction]

for inst in instruction:
    for idx in range(inst[0]):
        crates[inst[1] - 1], tmp = crates[inst[1] - 1][:-1], crates[inst[1] - 1][-1]
        crates[inst[2] - 1] += tmp

result = ""
for stack in crates:
    result += stack[-1]

print(result)
