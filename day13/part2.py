if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    n_cases = (len(lines) + 1) // 4
    result = 0
    for i in range(n_cases):
        conf = dict()

        conf_A = lines[4 * i].split(":")[1].strip().split(",")
        conf["A"] = {"X": int(conf_A[0][2:]), "Y": int(conf_A[1][3:])}
        conf_B = lines[4 * i + 1].split(":")[1].strip().split(",")
        conf["B"] = {"X": int(conf_B[0][2:]), "Y": int(conf_B[1][3:])}
        conf_prize = lines[4 * i + 2].split(":")[1].strip().split(",")
        conf["prize"] = {
            "X": 10000000000000 + int(conf_prize[0][2:]),
            "Y": 10000000000000 + int(conf_prize[1][3:]),
        }

        # System of equations, invert matrix and solve, keep only integer solutions
        a = conf["A"]["X"]
        b = conf["B"]["X"]
        c = conf["A"]["Y"]
        d = conf["B"]["Y"]
        denom = a * d - b * c
        if denom != 0:
            i = (d * conf["prize"]["X"] - b * conf["prize"]["Y"]) / denom
            j = (-c * conf["prize"]["X"] + a * conf["prize"]["Y"]) / denom
            if i == int(i) and j == int(j):
                cost = 3 * i + j

                result += cost

    print(int(result))
