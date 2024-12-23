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
        valid_update = True
        i = 0
        while i < len(pages):
            valid = True
            x = pages[i]
            j = i + 1
            while j < len(pages) and valid:
                y = pages[j]
                if x in ordering_rules[y]:
                    valid = False
                    valid_update = False
                else:
                    j += 1
            if not valid:
                tmp = pages[i]
                pages[i] = pages[j]
                pages[j] = tmp
            else:
                i += 1

        if not valid_update:
            result += pages[(len(pages) // 2)]

    print(result)
