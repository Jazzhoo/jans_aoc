with open("input.txt", "r") as f:
    supply_data = f.readlines()

max_cal = [0, 0, 0]
temp_calc = 0

for line in supply_data:
    if len(line.strip()) > 1:
        temp_calc += int(line.strip())
    else:
        if temp_calc > max_cal[2]:
            max_cal[2] = temp_calc
        temp_calc = 0
        max_cal.sort(reverse=True)
        continue
if temp_calc > max_cal[2]:
    max_cal[2] = temp_calc
temp_calc = 0
max_cal.sort(reverse=True)
print(f"max cal was: {sum(max_cal)}")
