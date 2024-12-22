import re


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        seq = "".join(f.read().splitlines())

    matches = re.finditer(r"(do(n\'t)?\(\))|(mul\(\d+,\d+\))", seq)
    result = 0
    status = True
    for match in matches:
        group = match.group()
        if group == "do()":
            status = True
        elif group == "don't()":
            status = False
        elif status:
            a, b = [int(x) for x in group[4:-1].split(",")]
            result += a * b

    print(result)
