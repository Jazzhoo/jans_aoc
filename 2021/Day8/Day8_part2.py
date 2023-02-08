def how_many_a_in_b(a: str, b: str):
    count = 0
    for char in a:
        if char in b:
            count += 1
    return count


with open("input_files/input.txt", "r") as f:
    code_lines = f.readlines()

code_lines_merged = [line.replace('|', '') for line in code_lines]
distorted_input_lines = [line.strip().split(' ') for line in code_lines_merged]
unique_numbers = [(1, 2), (4, 4), (7, 3), (8, 7)]  # (number, len)
decoded_numbers = ['' for a in range(0, 10)]
partially_decoded_numbers = [[], []]
result = 0

for line in distorted_input_lines:
    for idx in range(len(line)):
        line[idx] = ''.join(sorted(line[idx]))
    for num in line:
        if len(num) == 2:
            decoded_numbers[1] = num
        elif len(num) == 4:
            decoded_numbers[4] = num
        elif len(num) == 3:
            decoded_numbers[7] = num
        elif len(num) == 7:
            decoded_numbers[8] = num
        # now starting to move 5 and 6 segment numbers
        elif len(num) == 5:
            partially_decoded_numbers[0].append(num)
        elif len(num) == 6:
            partially_decoded_numbers[1].append(num)

    # decoding
    for num in partially_decoded_numbers[0]:
        if how_many_a_in_b(num, decoded_numbers[1]) == 2 or how_many_a_in_b(num, decoded_numbers[7]) == 3:
            decoded_numbers[3] = num
            continue
        elif how_many_a_in_b(num, decoded_numbers[4]) == 2:
            decoded_numbers[2] = num
            continue
        elif how_many_a_in_b(num, decoded_numbers[4]) == 3:
            decoded_numbers[5] = num
            continue

    for num in partially_decoded_numbers[1]:
        if how_many_a_in_b(num, decoded_numbers[7]) < 3:
            decoded_numbers[6] = num
            continue
        elif how_many_a_in_b(num, decoded_numbers[4]) == 4:
            decoded_numbers[9] = num
            continue
        else:
            decoded_numbers[0] = num
            continue ## TODO: Need to finish decoding
    partially_decoded_numbers = [[], []]

    temp_num = ""
    for num in line[len(line) - 4:]:
        temp_num += str(decoded_numbers.index(num))
    result += int(temp_num)

print(f"the result is: {result}")

