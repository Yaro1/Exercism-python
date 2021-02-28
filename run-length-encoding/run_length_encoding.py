from re import sub


def encode(s):
    return sub(r"(.)\1+", lambda x: str(len(x.group(0))) + x.group(1), s)


def decode(s):
    return sub(r"(\d+)(\D)", lambda x: x.group(2) * int(x.group(1)), s)