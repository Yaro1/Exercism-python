#31
def str_gen(d, x):
    return x + ' ' * (31 - len(x)) + '|  ' + str(d[x]['MP']) + ' |  ' + str(d[x]['W']) + ' |  ' + str(d[x]['D']) + ' |  ' + str(d[x]['L']) + ' |  ' + str(d[x]['P'])


def tally(rows):
    d = dict()
    rows = [x.split(';') for x in rows]
    for i in rows:

        if i[0] not in d.keys():
            d[i[0]] = {'MP': 0, 'W': 0, 'D': 0, 'P': 0, 'L': 0}

        d[i[0]]['MP'] += 1
        if i[2] == 'win':
            d[i[0]]['W'] += 1
            d[i[0]]['P'] += 3
        if i[2] == 'draw':
            d[i[0]]['D'] += 1
            d[i[0]]['P'] += 1
        if i[2] == 'loss':
            d[i[0]]['L'] += 1

        if i[1] not in d.keys():
            d[i[1]] = {'MP': 0, 'W': 0, 'D': 0, 'P': 0, 'L': 0}

        d[i[1]]['MP'] += 1
        if i[2] == 'win':
            d[i[1]]['L'] += 1
        if i[2] == 'draw':
            d[i[1]]['D'] += 1
            d[i[1]]['P'] += 1
        if i[2] == 'loss':
            d[i[1]]['W'] += 1
            d[i[1]]['P'] += 3

    str_ = ["Team                           | MP |  W |  D |  L |  P"]
    number_points = {}
    for i in d:
        if d[i]['P'] not in number_points:
            number_points[d[i]['P']] = [{i:d[i]}]
        else:
            number_points[d[i]['P']].append({i:d[i]})

    for i in reversed(sorted(number_points)):
        for j in sorted(number_points[i], key=lambda item: list(item.keys())[0]):
            str_.append(str_gen(j, list(j.keys())[0]))
    return str_
