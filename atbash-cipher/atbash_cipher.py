import re

alphabet = list("abcdefghijklmnopqrstuvwxyz")


def preparing(f):
    def wrapper(plain_text):
        plain_text = re.sub(r"[^a-zA-Z0-9 ]+", '', plain_text)
        new_text = ''.join([alphabet[25 - alphabet.index(i)] if i.isalpha() else i for i in plain_text.lower()])
        return f(new_text)
    return wrapper


@preparing
def encode(plain_text):
    plain_text = plain_text.replace(" ", "")
    new_text = ""
    for i in range(len(plain_text)):
        new_text = ''.join([new_text, ' ', plain_text[i]]) if i % 5 and i != 0 else ''.join([new_text, plain_text[i]])
    return new_text


@preparing
def decode(ciphered_text):
    ciphered_text = re.sub(r" ", "", ciphered_text)
    return ciphered_text


print("TEST BRANCH")