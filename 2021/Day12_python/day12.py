import collections
with open("./input_files/main_puzzle.txt", "r") as f:
#with open("./input_files/example_puzzle_2.txt", "r") as f:
# with open("./input_files/example_puzzle.txt", "r") as f:
        raw_input = f.readlines()

cave_map = collections.defaultdict(set)
for line in raw_input:
    src, dst = line.replace('\n', '').split('-')
    cave_map[src].add(dst)
    cave_map[dst].add(src)


def search_caves(map_of_caves: dict):
    paths_to_follow = [["start"]]
    paths_found = []

    while paths_to_follow:
        current_path = paths_to_follow.pop()
        current_cave = current_path[-1]

        for neighbour in map_of_caves[current_cave]:
            new_path = [*current_path, neighbour]
            if neighbour == "end":
                paths_found.append([*current_path, neighbour])
                continue
            if neighbour[0].isupper() or neighbour not in current_path:
                paths_to_follow.append(new_path)
    return len(paths_found)


pathsFound = search_caves(cave_map)
print(f'The number of path found: {pathsFound}')
