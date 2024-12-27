if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    N = 103
    M = 101
    n_seconds = 100
    quadrants = [0, 0, 0, 0]
    for line in lines:
        p, v = line.split(" ")
        p = p.split(",")
        px, py = int(p[0][2:]), int(p[1])
        v = v.split(",")
        vx, vy = int(v[0][2:]), int(v[1])

        px = (px + n_seconds * vx) % M
        py = (py + n_seconds * vy) % N

        if px < M // 2:
            if py < N // 2:
                quadrants[0] += 1
            elif py > N // 2:
                quadrants[1] += 1
        elif px > M // 2:
            if py < N // 2:
                quadrants[2] += 1
            elif py > N // 2:
                quadrants[3] += 1

    result = 1
    for i in range(4):
        result *= quadrants[i]

    print(result)
