directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    N = len(data)
    M = len(data[0])

    result = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "X":
                for x, y in directions:
                    pos_M = (i + x, j + y)
                    if (
                        pos_M[0] >= 0
                        and pos_M[0] <= N - 1
                        and pos_M[1] >= 0
                        and pos_M[1] <= M - 1
                        and data[pos_M[0]][pos_M[1]] == "M"
                    ):
                        pos_A = (i + 2 * x, j + 2 * y)
                        if (
                            pos_A[0] >= 0
                            and pos_A[0] <= N - 1
                            and pos_A[1] >= 0
                            and pos_A[1] <= M - 1
                            and data[pos_A[0]][pos_A[1]] == "A"
                        ):
                            pos_S = (i + 3 * x, j + 3 * y)
                            if (
                                pos_S[0] >= 0
                                and pos_S[0] <= N - 1
                                and pos_S[1] >= 0
                                and pos_S[1] <= M - 1
                                and data[pos_S[0]][pos_S[1]] == "S"
                            ):
                                result += 1

    print(result)
