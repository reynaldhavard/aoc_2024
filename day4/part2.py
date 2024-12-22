POSITIONS_OFFSETS = [
    [(0, 2), (1, 1), (2, 0), (2, 2)],
    [(0, 2), (-1, 1), (-2, 0), (-2, 2)],
    [(2, 0), (1, 1), (0, 2), (2, 2)],
    [(2, 0), (1, -1), (0, -2), (2, -2)],
]
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    N = len(data)
    M = len(data[0])

    result = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == "M":
                for offsets in POSITIONS_OFFSETS:
                    pos_M = (i + offsets[0][0], j + offsets[0][1])
                    if (
                        pos_M[0] >= 0
                        and pos_M[0] <= N - 1
                        and pos_M[1] >= 0
                        and pos_M[1] <= M - 1
                        and data[pos_M[0]][pos_M[1]] == "M"
                    ):
                        pos_A = (i + offsets[1][0], j + offsets[1][1])
                        if (
                            pos_A[0] >= 0
                            and pos_A[0] <= N - 1
                            and pos_A[1] >= 0
                            and pos_A[1] <= M - 1
                            and data[pos_A[0]][pos_A[1]] == "A"
                        ):
                            pos_S1 = (i + offsets[2][0], j + offsets[2][1])
                            pos_S2 = (i + offsets[3][0], j + offsets[3][1])
                            if (
                                pos_S1[0] >= 0
                                and pos_S1[0] <= N - 1
                                and pos_S1[1] >= 0
                                and pos_S1[1] <= M - 1
                                and data[pos_S1[0]][pos_S1[1]] == "S"
                                and pos_S2[0] >= 0
                                and pos_S2[0] <= N - 1
                                and pos_S2[1] >= 0
                                and pos_S2[1] <= M - 1
                                and data[pos_S2[0]][pos_S2[1]] == "S"
                            ):
                                result += 1

    print(result)
