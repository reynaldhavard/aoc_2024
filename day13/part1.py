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
        conf["prize"] = {"X": int(conf_prize[0][2:]), "Y": int(conf_prize[1][3:])}

        min_cost = None
        i = 0
        while (
            i * conf["A"]["X"] <= conf["prize"]["X"]
            and i * conf["A"]["Y"] <= conf["prize"]["Y"]
            and i <= 100
        ):
            remain_X = conf["prize"]["X"] - i * conf["A"]["X"]
            remain_Y = conf["prize"]["Y"] - i * conf["A"]["Y"]
            jX = remain_X / conf["B"]["X"]
            jY = remain_Y / conf["B"]["Y"]
            if jX == jY and jX == int(jX) and jX <= 100:
                cost = 3 * i + jX
                if min_cost is None or cost < min_cost:
                    min_cost = cost
            i += 1

        if min_cost is not None:
            result += min_cost

    print(int(result))
