def is_prime(i):
    for j in range(2, int(i ** 0.5)):
        if i % j == 0:
            return False
    return True


def factors(value):
    answer, i = [], 2
    while i <= value:
        if value % i == 0 and is_prime(i):
            answer.append(i)
            value, i = value / i, 2
        else:
            i += 1
    return answer
