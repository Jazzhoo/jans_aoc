file = open("input", "r")
report = file.readlines()
report = [i[:-1] for i in report]

gama_rate = [0 for i in report[0]]

for line in report:
    for k, digit in enumerate(line):
        gama_rate[k] += int(digit)

gama_rate = [1 if i > len(report)/2 else 0 for i in gama_rate]
epsilon_rate = [1 if i == 0 else 0 for i in gama_rate]

gama_rate = ''.join(str(e) for e in gama_rate)
epsilon_rate = ''.join(str(e) for e in epsilon_rate)
power_consumption = int(''.join(gama_rate), 2) * int(''.join(epsilon_rate), 2)

print(f"Power consumption: {power_consumption}")
pass