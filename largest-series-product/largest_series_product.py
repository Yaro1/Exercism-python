def largest_product(series, size):
    if size == 0:
        return 1
    # Exceptions, Errors:
    if len(series) < size:
        raise ValueError("Size is larger than the whole series!")
    if size < 0:
        raise ValueError("How can size be negative?!")
    answer = [0]
    prod = [0]*len(series)
    cum = 1
    for i in range(len(series)):
        if series[i] != "0":
            cum *= int(series[i])
            prod[i] = cum
        else:
            cum = 1
    i = 0
    count = 0
    while i < len(prod):
        if prod[i] == 0:
            i += 1
            count = 0
        else:
            count += 1
            if count == size:
                if i >= size and prod[i - size] > 0:
                    answer.append(prod[i] // prod[i - size])
                else:
                    answer.append(prod[i])
                count -= 1
            i += 1
    return max(answer)
