if __name__ == "__main__":
    with open("input.txt", "r") as f:
        garden = f.read().splitlines()

    N = len(garden)
    M = len(garden[0])

    perimeters = dict()
    areas = dict()
    pos_to_region = [[-1 for _ in range(M)] for _ in range(N)]

    n_region = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue

            region_type = garden[i][j]
            pos_to_region[i][j] = n_region
            next_pos = [(i, j)]
            while len(next_pos) > 0:
                a, b = next_pos.pop()
                if garden[a][b] == region_type:
                    for offset in offsets:
                        ia = a + offset[0]
                        ib = b + offset[1]
                        if (
                            ia >= 0
                            and ia <= N - 1
                            and ib >= 0
                            and ib <= M - 1
                            and not visited[ia][ib]
                            and garden[ia][ib] == region_type
                        ):
                            visited[ia][ib] = True
                            pos_to_region[ia][ib] = n_region
                            next_pos.append((ia, ib))

            n_region += 1

    for i in range(N):
        for j in range(M):
            region = pos_to_region[i][j]
            areas[region] = areas.get(region, 0) + 1
            if i == 0 or pos_to_region[i - 1][j] != region:
                perimeters[region] = perimeters.get(region, 0) + 1
            if j == 0 or pos_to_region[i][j - 1] != region:
                perimeters[region] = perimeters.get(region, 0) + 1
            if i == N - 1 or pos_to_region[i + 1][j] != region:
                perimeters[region] = perimeters.get(region, 0) + 1
            if j == M - 1 or pos_to_region[i][j + 1] != region:
                perimeters[region] = perimeters.get(region, 0) + 1

    result = 0
    for region_type in perimeters:
        result += perimeters[region_type] * areas[region_type]

    print(result)
