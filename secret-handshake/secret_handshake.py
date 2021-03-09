d_ = {0: "wink", 1: "double blink", 2: "close your eyes", 3: "jump", 4: "rev"}


def commands(number):
    if number == 0:
        return []
    str_ = bin(number)[2:]
    answer = [d_[j] for i, j in zip(reversed(str_), range(len(str_))) if i == "1"]
    if answer[-1] == "rev":
        return list(reversed(answer[:len(answer) - 1]))
    else:
        return answer
