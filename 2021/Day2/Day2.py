
lines = []
X = 0
Y = 0

with open("day2_input", "r") as f:
    lines = f.readlines()

for line in lines:
    temp_x, temp_y = line.split()
    if temp_x == "forward":
        X += int(temp_y)
    elif temp_x == "down":
        Y += int(temp_y)
    elif temp_x == "up":
        Y -= int(temp_y)

print(f"X:{X}, Y:{Y}, result:{X*Y}")