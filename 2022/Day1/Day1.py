with open("input.txt", "r") as f:
    supply_data = f.readlines()

max_cal = 0
temp_calc = 0

for line in supply_data:
    if len(line.strip()) > 1:
        temp_calc += int(line.strip())
    else:
        if temp_calc > max_cal:
            max_cal = temp_calc
        temp_calc = 0
        continue
print(f"max cal was: {max_cal}")
