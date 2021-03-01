def flatten_1(iterable):
    answer = []
    if type(iterable) is list:
        for i in iterable:
            answer += flatten(i)
    elif iterable is not None:
        answer.append(iterable)
    return answer


def flatten_generator(iterable):
    for i in iterable:
        if type(i) is list:
            yield from flatten_generator(i)
        elif i is not None:
            yield i


def flatten(iterable):
    return list(flatten_generator(iterable))
