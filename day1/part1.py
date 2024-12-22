import numpy as np


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    list1 = []
    list2 = []
    for line in lines:
        int1, int2 = [int(s) for s in line.split() if s.isdigit()]
        list1.append(int1)
        list2.append(int2)

    list1 = np.array(sorted(list1))
    list2 = np.array(sorted(list2))

    result = np.sum(np.abs(list1 - list2))

    print(result)
