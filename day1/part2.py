if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    list1 = []
    list2 = []
    for line in lines:
        int1, int2 = [int(s) for s in line.split() if s.isdigit()]
        list1.append(int1)
        list2.append(int2)

    counts1 = dict()
    counts2 = dict()
    for x in list2:
        counts2[x] = counts2.get(x, 0) + 1

    result = 0
    for x in list1:
        result += x * counts2.get(x, 0)

    print(result)
