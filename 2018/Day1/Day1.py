#function to use for 2nd part of Day 1
result =0 
def calcFuel(mass):
    fuel = int(mass/3-2)
    if fuel < 0:
        return 0
    else:
        return fuel + calcFuel(fuel)


#Day 1 main
with open("/home/jazzhoo/Dropbox/Code/AdventOfCode/Day1_input", "r") as f:
    for line in f.readlines():
        result=result+calcFuel(int(line))
print(result)
         