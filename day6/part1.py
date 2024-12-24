if __name__ == "__main__":
    with open("input.txt", "r") as f:
        grid = f.read().splitlines()

    # Find original position and direction
    N = len(grid)
    M = len(grid[0])
    visited_positions = [[0 for _ in range(M)] for _ in range(N)]

    orig_pos_found = False
    cur_i, cur_j = -1, -1
    dir = (-1, 0)
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "^":
                orig_pos_found = True
                cur_i = i
                cur_j = j
                break
        if orig_pos_found:
            break

    while cur_i >= 0 and cur_i < N and cur_j >= 0 and cur_j < M:
        visited_positions[cur_i][cur_j] = 1
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

    result = sum(sum(x) for x in visited_positions)

    print(result)
