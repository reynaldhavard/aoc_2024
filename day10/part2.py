if __name__ == "__main__":
    with open("sample2.txt", "r") as f:
        topo_map_str = f.read().splitlines()

    topo_map = [[int(s) for s in row] for row in topo_map_str]
    N = len(topo_map)
    M = len(topo_map[0])

    visited = [[0 for _ in range(M)] for _ in range(N)]
    connections = [[0 for _ in range(M)] for _ in range(N)]
    start_pos = set()
    id = 0
    for i in range(N):
        for j in range(M):
            if topo_map[i][j] == 0:
                start_pos.add((i, j))
                connections[i][j] += 1
                id += 1

    next_level = 1
    while len(start_pos) > 0:
        next_pos = set()
        for i, j in start_pos:
            for a, b in [
                (i, j - 1),
                (i, j + 1),
                (i - 1, j),
                (i + 1, j),
            ]:
                if (
                    a >= 0
                    and a < N
                    and b >= 0
                    and b < M
                    and topo_map[a][b] == next_level
                ):
                    next_pos.add((a, b))
                    connections[a][b] += connections[i][j]

        start_pos = next_pos
        next_level += 1
        if next_level == 10:
            break

    result = 0
    for i, j in start_pos:
        result += connections[i][j]

    print(result)
