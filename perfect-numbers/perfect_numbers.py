def find_delimetres(number):
    answer = []
    for i in range(1, int(number ** 0.5) + 1):
        if not number % i:
            answer += list(set([i, number // i])) if number // i != number else [i]
    return answer


def classify(number):
    if number <= 0:
        raise ValueError("Wrong number!")
    if number == 1:
        return "deficient"
    s = sum(find_delimetres(number))
    if s == number:
        return "perfect"
    elif s > number:
        return "abundant"
    else:
        return "deficient"
