import numpy as np
with open('example_input.txt', 'r') as f:
    initial_state = f.readlines()

initial_state = initial_state[0].split(',')
initial_state = [int(a) for a in initial_state]
fish_school = np.array(initial_state)

days_to_count = 256

for day in range(1, days_to_count + 1, 1):
    fish_school = fish_school - 1
    negative_fish = fish_school < 0
    new_fish = negative_fish.astype(int)
    fish_school = fish_school + new_fish * 7
    new_fish = np.sum(new_fish)
    if new_fish > 0:
        new_fish = np.full((1, new_fish), 8)
        fish_school = np.append(fish_school, new_fish)

    #print(f'After day {day}: {fish_school}')
    print(f'After day {day}: There is {len(fish_school)}')
print(f'The full school counts: {len(fish_school)}')
pass