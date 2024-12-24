from collections import defaultdict


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        grid = f.read().splitlines()

    N = len(grid)
    M = len(grid[0])

    antennas_location = defaultdict(list)
    antinodes_location = set()
    for i in range(N):
        for j in range(M):
            if grid[i][j] != ".":
                for antenna in antennas_location[grid[i][j]]:
                    ii, jj = antenna
                    diff_i = i - ii
                    diff_j = j - jj

                    t = 0
                    ia, ja = ii, jj
                    while ia >= 0 and ia < N and ja >= 0 and ja < M:
                        antinodes_location.add((ia, ja))
                        t += 1
                        ia = (t + 1) * ii - t * i
                        ja = (t + 1) * jj - t * j

                    t = 0
                    ib, jb = i, j
                    while ib >= 0 and ib < N and jb >= 0 and jb < M:
                        antinodes_location.add((ib, jb))
                        t += 1
                        ib = (t + 1) * i - t * ii
                        jb = (t + 1) * j - t * jj

                antennas_location[grid[i][j]].append((i, j))

    print(len(antinodes_location))
