import re


def cipher_text(plain_text):
    if plain_text == "":
        return ""
    normalized = ''.join(filter(str.isalnum, plain_text.lower()))
    square = int(len(normalized)**0.5) if int(len(normalized)**0.5)**2 == len(normalized) else int(len(normalized)**0.5)+1
    tmp = len(normalized) // square
    r, c = square, tmp if tmp*square >= len(normalized) else tmp+1
    if r > c:
        r, c = c, r
    if r != c:
        answer = ''.join([normalized[j] for i in range(0, r+1) for j in range(i, len(normalized), c)])
    else:
        answer = ''.join([normalized[j] for i in range(0, r) for j in range(i, len(normalized), c)])
    number_space = r*c - len(normalized)
    head_list = [answer[i:i+r] for i, j in zip(range(0, len(answer), r), range(c-number_space))]
    if number_space > 0:
        tail_list = [answer[i:i+r-1]+' ' for i in range(r*(c-number_space), len(answer), r-1)]
    else:
        tail_list = []
    return ' '.join(head_list+tail_list)