import re


def is_pangram(sentence):
    sentence = ''.join(re.findall("[a-zA-Z]", sentence)).lower().replace(" ", "")
    return len(set(sentence)) == 26