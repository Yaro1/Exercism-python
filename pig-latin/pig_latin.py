def translate(text):
    answer = []
    for t in text.split():
        next_symbols = ""
        if t[0] not in 'eyuioax' or (t[0] == 'x' and t[1] in 'euioa') or (t[0] == 'y' and t[1] in 'euioa'):
            it = 1
            while t[it] not in 'euioay':
                it += 1
            if 'qu' in t[it-1:it+1]:
                t, next_symbols = t[it+1:], t[:it+1]
            else:
                t, next_symbols = t[it:], t[:it]
        answer.append(''.join([t, next_symbols, 'ay']))
    return ' '.join(answer)