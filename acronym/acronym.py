import re


def abbreviate(words):
    return ''.join([i[0].upper() for i in re.split("""[- |,\n\t!.?"':&@$%^_#]""", words.replace("'t", "").replace("'s", "")) if i != ''])