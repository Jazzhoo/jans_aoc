class helper_functions:

    @staticmethod
    def check_if_lowest(heat_map, x, y):
        shape = heat_map.shape
        a = heat_map[x, y]
        lowest = True
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for move in moves:
            nx = x + move[0]
            ny = y + move[1]

            if nx < 0 or nx >= shape[0]:
                b = 10
            elif ny < 0 or ny >= shape[1]:
                b = 10
            else:
                b = heat_map[nx, ny]

            if a >= b:
                lowest = False
                break
        return lowest

    @staticmethod
    def traverse_deeper(height_map, point: tuple[int, int], visited: [tuple[int, int]]) -> [tuple[int, int]]:
        shape = height_map.shape
        row, col = point
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        b = []

        for move in moves:
            nrow = row + move[0]
            ncol = col + move[1]

            if nrow < 0 or nrow >= shape[0]:
                continue
            elif ncol < 0 or ncol >= shape[1]:
                continue
            elif height_map[nrow, ncol] == 9:
                continue
            elif (nrow, ncol) in visited:
                continue
            else:
                b.append((nrow, ncol))
                visited.append((nrow, ncol))

        return b
