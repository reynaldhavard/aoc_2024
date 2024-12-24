class Position:
    def __init__(self):
        self.dirs_when_visited = set()
        self.visited_ver = False
        self.visited_hor = False

    def add_dir_when_visited(self, dir):
        self.dirs_when_visited.add(dir)
        if dir[0] == 0:
            self.visited_hor = True
        else:
            self.visited_ver = True

    def has_dir_been_visited(self, dir):
        return dir in self.dirs_when_visited


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        grid = f.read().splitlines()

    N = len(grid)
    M = len(grid[0])

    orig_pos_found = False
    orig_i, orig_j = -1, -1
    dir = (-1, 0)
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "^":
                orig_pos_found = True
                orig_i, orig_j = i, j
                break
        if orig_pos_found:
            break

    cur_i, cur_j = orig_i, orig_j
    positions_set = set()
    while cur_i >= 0 and cur_i < N and cur_j >= 0 and cur_j < M:
        positions_set.add((cur_i, cur_j))
        if (
            cur_i + dir[0] >= 0
            and cur_i + dir[0] < N
            and cur_j + dir[1] >= 0
            and cur_j + dir[1] < M
            and grid[cur_i + dir[0]][cur_j + dir[1]] == "#"
        ):
            dir = (dir[1], -dir[0])
        else:
            cur_i += dir[0]
            cur_j += dir[1]

    result = 0
    for a, b in positions_set:
        if a == orig_i and b == orig_j:
            continue

        visited_positions_w_obs = [[Position() for _ in range(M)] for _ in range(N)]
        cur_i, cur_j = orig_i, orig_j
        dir = (-1, 0)
        while cur_i >= 0 and cur_i < N and cur_j >= 0 and cur_j < M:
            if visited_positions_w_obs[cur_i][cur_j].has_dir_been_visited(dir):
                result += 1
                break
            visited_positions_w_obs[cur_i][cur_j].add_dir_when_visited(dir)
            if (
                cur_i + dir[0] >= 0
                and cur_i + dir[0] < N
                and cur_j + dir[1] >= 0
                and cur_j + dir[1] < M
                and (
                    grid[cur_i + dir[0]][cur_j + dir[1]] == "#"
                    or (cur_i + dir[0] == a and cur_j + dir[1] == b)
                )
            ):
                dir = (dir[1], -dir[0])
            else:
                cur_i += dir[0]
                cur_j += dir[1]

    print(result)
