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
            if grid[i][j] != '.':
                for antenna in antennas_location[grid[i][j]]:
                    ii, jj = antenna
                    diff_i = i - ii
                    diff_j = j - jj

                    ia, ja = 2*ii - i, 2*jj - j
                    ib, jb = 2*i - ii, 2*j - jj
                    if ia >= 0 and ia < N and ja >= 0 and ja < M:
                        antinodes_location.add((ia, ja))
                    if ib >= 0 and ib < N and jb >= 0 and jb < M:
                        antinodes_location.add((ib, jb))

                antennas_location[grid[i][j]].append((i, j))


    print(len(antinodes_location))
