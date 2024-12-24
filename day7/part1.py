def check_if_input_possible(test_input, values):
    totals_step = {values[0]}
    for value in values[1:]:
        new_totals = set()
        for total_step in totals_step:
            if total_step + value <= test_input:
                new_totals.add(total_step + value)
            if total_step * value <= test_input:
                new_totals.add(total_step * value)
        totals_step = new_totals

    return test_input in totals_step


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    result = 0
    for line in lines:
        test_input, values = line.split(":")
        test_input = int(test_input)
        values = [int(s) for s in values.strip().split(" ")]
        if check_if_input_possible(test_input, values):
            result += test_input

    print(result)
