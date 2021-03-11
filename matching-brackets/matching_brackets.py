import re

brackets = ["(", ")", "[", "]", "{", "}"]


def check(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')
    return not text


def is_paired(input_string):
    return check(''.join(filter(lambda x: x in brackets, input_string)))