filepath = "input.txt"
content = []
with open(filepath) as f:
    content = f .readlines()


content = [int(f.strip("\n")) for f in content]
#print(content)

for i,x in enumerate(content):
    for y in content[i::]:
        if x + y == 2020:
            print(f"{x} + {y} == 2020 and the answer is {x*y}")
            break