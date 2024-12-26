if __name__ == "__main__":
    with open("input.txt", "r") as f:
        stones = [int(s) for s in f.read().splitlines()[0].split(" ")]

    # No need to save order to solve task
    stones_dict = {}
    for stone in stones:
        stones_dict[stone] = stones_dict.get(stone, 0) + 1

    for _ in range(75):
        updated_stones = dict()
        for stone in stones_dict:
            if stone == 0:
                updated_stones[1] = updated_stones.get(1, 0) + stones_dict[stone]
            elif len(str(stone)) % 2 == 0:
                n = len(str(stone))
                str_stone = str(stone)
                x = int(str_stone[: n // 2])
                y = int(str_stone[n // 2 :])
                updated_stones[x] = updated_stones.get(x, 0) + stones_dict[stone]
                updated_stones[y] = updated_stones.get(y, 0) + stones_dict[stone]
            else:
                updated_stones[2024 * stone] = (
                    updated_stones.get(2024 * stone, 0) + stones_dict[stone]
                )
        stones_dict = updated_stones

    result = 0
    for stone in stones_dict:
        result += stones_dict[stone]

    print(result)
