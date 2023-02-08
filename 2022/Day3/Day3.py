import numpy as np

with open("input.txt", "r") as f:
    inventory = f.readlines()


score ="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0
inventory = [x.strip() for x in inventory]
for line in inventory:
    half = int(len(line)/2)
    for chr in line[:half]:
        if line[half:].count(chr) > 0:
            total += score.index(chr)
            break
print(total)

