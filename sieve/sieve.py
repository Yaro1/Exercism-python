def generator(num, end):
    j = num ** 2
    while j <= end:
        yield j
        j = j + num


def primes(limit):
    a = [True for i in range(limit)]
    for i in range(limit):
        if a[i] is True and i + 1 > 1:
            for j in generator(i + 1, limit):
                a[j - 1] = False

    return [i + 1 for i in range(1, limit) if a[i] is True]

# 0.039s - Check each element for j
# 0.011s - Check elements by formula: i^2 + n*i
