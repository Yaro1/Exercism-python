str_1 = [" bottles of beer on the wall, ", " bottles of beer."]
str_2 = ["Take one down and pass it around, ", " bottles of beer on the wall."]
str_end = ["No more bottles of beer on the wall, no more bottles of beer.",
           "Go to the store and buy some more, 99 bottles of beer on the wall."]
str_one = ["1 bottle of beer on the wall, 1 bottle of beer.",
           "Take it down and pass it around, no more bottles of beer on the wall.", ]
str_one_down = "Take one down and pass it around, 1 bottle of beer on the wall."

f = (lambda start: [''.join([str(start), str_1[0], str(start), str_1[1]]),
                    ''.join([str_2[0], str(start - 1), str_2[1]])
                    ])


def recite(start, take=1):
    answer = []
    if start == 0:
        return str_end
    for i, j in zip(range(start, 1, -1), range(take)):
        answer = answer + f(i) + [""] if i > 2 else answer + [f(i)[0], str_one_down ,""]
    if start <= take:
        answer += str_one
        return answer + (take - start) * ["", str_end[0], str_end[1]]
    else:
        return answer[:len(answer) - 1]
