def is_valid(isbn):
    str_ = isbn.replace("-", "")
    if len(str_) != 10:
        return False
    num = 0
    for i, j in zip(reversed(str_), range(1, 11)):
        if not i.isdigit() and i != "X":
            return False
        if i == "X" and j != 1:
            return False
        num += int(i)*j if i != "X" else 10*j
    return num % 11 == 0