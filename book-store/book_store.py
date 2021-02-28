price_dict = {1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}


def total(basket):
    groups = []
    while basket:
        g = set(basket)
        groups.append(len(g))
        for i in g:
            basket.remove(i)
    while 3 in groups and 5 in groups:
        groups.remove(3)
        groups.remove(5)
        groups += [4, 4]
    return sum([price_dict[i] for i in groups])
