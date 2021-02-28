import re


def count_words(sentence):
    str_ = [i.replace("=t", "'t") for i in re.split("""[ |,\n\t!.?"':&@$%^_]""",
            sentence.lower().replace(" 't", " ,t").replace("'t", "=t")) if i != '']
    return dict([(x, sum(x == i for i in str_)) for x in str_])


print(count_words("Joe can't tell between app, apple and a."))