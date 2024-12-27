import math


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    N = 103
    M = 101
    for n_seconds in range(101 * 103):
        distinct_x = []
        distinct_y = []
        grid = [[0 for _ in range(M)] for _ in range(N)]
        valid = True
        for line in lines:
            p, v = line.split(" ")
            p = p.split(",")
            px, py = int(p[0][2:]), int(p[1])
            v = v.split(",")
            vx, vy = int(v[0][2:]), int(v[1])

            px = (px + n_seconds * vx) % M
            py = (py + n_seconds * vy) % N

            if grid[py][px] != 0:
                valid = False
                break
            grid[py][px] += 1
        if valid:
            print("\n\n", n_seconds)
            for i in range(N):
                for j in range(M):
                    if grid[i][j] == 0:
                        print(".", end="")
                    else:
                        print(grid[i][j], end="")
                print("\n", end="")
