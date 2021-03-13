def gen(l_, i=0):
    while i < len(l_):
        try:
            if l_[i] == 'minus' or l_[i] == 'plus':
                yield ('-', int(l_[i+1])) if l_[i] == 'minus' else ('+', int(l_[i+1]))
                i += 2
            elif l_[i] == 'multiplied' or l_[i] == 'divided':
                yield ('/', int(l_[i + 2])) if l_[i] == 'divided' else ('*', int(l_[i + 2]))
                i += 3
            else:
                yield "err", -1
        except IndexError:
            yield "err", -1


def answer(question):
    l_question = ''.join(filter(lambda x: x.isalnum() or x == ' ' or x == '-', question)).split()
    try:
        num = int(l_question[2])
        for i in gen(l_question[3:]):
            if i[0] == "+":
                num += i[1]
            elif i[0] == "-":
                num -= i[1]
            elif i[0] == "*":
                num *= i[1]
            elif i[0] == "/":
                num /= i[1]
            else:
                raise ValueError("Error")
        return num
    except IndexError:
        raise ValueError("Error")