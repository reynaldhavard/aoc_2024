if __name__ == "__main__":
    with open("input.txt", "r") as f:
        stones = [int(s) for s in f.read().splitlines()[0].split(" ")]

    for _ in range(25):
        updated_stones = []
        for stone in stones:
            if stone == 0:
                updated_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                n = len(str(stone))
                str_stone = str(stone)
                updated_stones.append(int(str_stone[: n // 2]))
                updated_stones.append(int(str_stone[n // 2 :]))
            else:
                updated_stones.append(stone * 2024)
        stones = updated_stones

    print(len(stones))
