with open('input.txt', 'r') as f:
    initial_state = f.readlines()

initial_state = initial_state[0].split(',')
initial_state = [int(a) for a in initial_state]
fish_school = initial_state.copy()

days_to_count = 80

for day in range(1, days_to_count + 1, 1):
    new_fish = 0
    for idx in range(len(fish_school)):
        if fish_school[idx] == 0:
            fish_school[idx] = 6
            new_fish = new_fish + 1
        else:
            fish_school[idx] = fish_school[idx] - 1
    for i in range(new_fish):
        fish_school.append(int(8))
    #print(f'After day {day}: {fish_school}')
    print(f'After day {day}: There is {len(fish_school)}')
print(f'The full school counts: {len(fish_school)}')
pass