from collections import defaultdict


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read()

    ordering_lines, update_lines = lines.split("\n\n")
    ordering_lines = ordering_lines.splitlines()
    update_lines = update_lines.splitlines()

    ordering_rules = defaultdict(set)
    for line in ordering_lines:
        x, y = [int(s) for s in line.split("|")]
        ordering_rules[x].add(y)

    result = 0
    for update in update_lines:
        pages = [int(s) for s in update.split(",")]
        valid = True
        for i in range(len(pages)):
            x = pages[i]
            for j in range(i+1, len(pages)):
                y = pages[j]
                if x in ordering_rules[y]:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            result += pages[(len(pages)//2)]

    print(result)


