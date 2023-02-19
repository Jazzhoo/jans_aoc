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
