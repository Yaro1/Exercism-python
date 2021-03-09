def is_prime(i):
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            return False
    return True


def generator_prime():
    i = 1
    while True:
        if is_prime(i):
            yield i
        i += 1


def prime(number):
    if number == 0:
        raise ValueError("There isn't any value.")
    for i, j in zip(generator_prime(), range(100000000)):
        if j == number:
            return i
