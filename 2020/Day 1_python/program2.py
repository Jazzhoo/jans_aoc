filepath = "input.txt"
content = []
with open(filepath) as f:
    content = f .readlines()


content = [int(f.strip("\n")) for f in content]
#print(content)

for i,x in enumerate(content):
    for j,y in enumerate(content[i::]):
        for k,z in enumerate(content[j::]):
            if (x + y + z == 2020):
                print(f"{x} + {y} + {z}== 2020 and the answer is {x*y*z}")
                break