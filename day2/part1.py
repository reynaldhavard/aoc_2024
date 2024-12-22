import numpy as np


def check_valid_report(report):
    last_el = report[0]
    dir = 1 if report[0] < report[1] else -1

    for x in report[1:]:
        abs_diff = np.abs(x - last_el)
        if (x - last_el) * dir > 0 and abs_diff >= 1 and abs_diff <= 3:
            last_el = x
        else:
            return False

    return True


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    reports = [[int(x) for x in line.split()] for line in lines]

    result = sum([check_valid_report(report) for report in reports])

    print(result)
