def frame(x, y):
    yield from ((x-1, y-1), (x-1, y), (x-1, y+1),
                (x, y-1), (x, y+1),
                (x+1, y-1), (x+1, y), (x+1, y+1))


def annotate(input_board_array):
    if any(len(x) != len(input_board_array[0]) for x in input_board_array):
        raise ValueError("Non uniform board lengths")

    out = [[0 if x == '0' else x for x in row.replace(' ', '0')]
           for row in input_board_array]

    for y, row in enumerate(input_board_array):
        for x, square in enumerate(row):
            if square != '*':
                if square != ' ':
                    raise ValueError("Illegal character")
                continue
            for xx, yy in frame(x, y):
                if (
                    0 <= xx < len(row) and
                    0 <= yy < len(input_board_array) and
                    out[yy][xx] != '*'
                ):
                    out[yy][xx] += 1

    return [''.join(str(x) if x != 0 else ' ' for x in row) for row in out]