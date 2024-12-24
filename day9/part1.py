if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read().splitlines()[0]

    list_input = []
    status_on = True
    id = 0
    for val in input:
        if status_on:
            list_input.extend([id for _ in range(int(val))])
            status_on = False
            id += 1
        else:
            list_input.extend(['.' for _ in range(int(val))])
            status_on = True

    i, j = 0, len(list_input) - 1
    result = 0
    while (i < j):
        if list_input[i] != '.':
            result += i * list_input[i]
            i += 1
        elif list_input[j] == '.':
            j -= 1
        else:
            tmp = list_input[i]
            list_input[i] = list_input[j]
            list_input[j] = tmp

    print(result)


