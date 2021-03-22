image_d = {(" _ ", "| |", "|_|"): "0",
           ("   ", "  |", "  |"): "1",
           (" _ ", " _|", "|_ "): "2",
           (" _ ", " _|", " _|"): "3",
           ("   ", "|_|", "  |"): "4",
           (" _ ", "|_ ", " _|"): "5",
           (" _ ", "|_ ", "|_|"): "6",
           (" _ ", "  |", "  |"): "7",
           (" _ ", "|_|", "|_|"): "8",
           (" _ ", "|_|", " _|"): "9"
           }


def divide_by_token(input_grid):
    length = len(input_grid[0]) // 3
    items_list = [[] for _ in range(length + length * (len(input_grid) // 4 - 1))]
    ind_jump, numbers_jump = 3, 0
    for i in range(len(input_grid)):
        if i == ind_jump:
            ind_jump, numbers_jump = ind_jump + 4, numbers_jump + 1
            continue
        for j, ind in zip(range(3, len(input_grid[0]) + 3, 3), range(len(input_grid[0]))):
            items_list[numbers_jump * length + ind].append(input_grid[i][j - 3:j])
    return items_list


def check_correct(f):
    def wrapper(input_grid):
        if sum([len(i) % 3 == 0 for i in input_grid]) == len(input_grid) and len(input_grid) % 4 == 0:
            return f(input_grid)
        else:
            raise ValueError("Not correct entering!")
    return wrapper


@check_correct
def convert(input_grid):
    str_ = ''.join([image_d[tuple(i)] if tuple(i) in image_d.keys() else "?" for i in divide_by_token(input_grid)])
    if len(input_grid) > 4:
        for i in range(len(input_grid) // 4 - 1):
            str_ = str_[:3 + i * 4] + "," + str_[3 + i * 4:]
    return str_
