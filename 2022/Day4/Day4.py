with open("input.txt", "r") as f:
    assignments = f.readlines()

assignments = [pair.strip().split(',') for pair in assignments]
assignments = [[pair[0].split('-'), pair[1].split('-')] for pair in assignments]
assignments = [[list(map(int, one)) for one in pair] for pair in assignments]

count = 0

for line in assignments:
    a = line[0]
    b = line[1]

    if (a[0] >= b[0] and a[1] <= b[1]) or (a[0] <= b[0] and a[1] >= b[1]):
        count += 1

print(f"overlaps {count}")
