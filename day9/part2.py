class Block:
    def __init__(self, id, pos, span):
        self.id = id
        self.pos = pos
        self.span = span

    def compute_value(self):
        result = 0
        for i in range(self.span):
            result += self.id * (self.pos + i)

        return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read().splitlines()[0]

    list_full_blocks = []
    list_empty_blocks = []
    status_on = True
    id = 0
    pos = 0
    for val in input:
        int_val = int(val)
        if status_on:
            list_full_blocks.append(Block(id=id, pos=pos, span=int_val))
            pos += int_val
            status_on = False
            id += 1
        else:
            list_empty_blocks.append(Block(id=".", pos=pos, span=int_val))
            pos += int_val
            status_on = True

    result = 0
    for i in range(len(list_full_blocks) - 1, -1, -1):
        full_block = list_full_blocks[i]
        start_full = full_block.pos
        span_full = full_block.span
        for j in range(len(list_empty_blocks)):
            empty_block = list_empty_blocks[j]
            start_empty = empty_block.pos
            if start_full < start_empty:
                break

            span_empty = empty_block.span
            if span_full <= span_empty:
                full_block.pos = start_empty
                empty_block.pos = start_empty + span_full
                empty_block.span = span_empty - span_full
                list_full_blocks[i] = full_block
                list_empty_blocks[j] = empty_block
                break
        result += list_full_blocks[i].compute_value()

    print(result)
