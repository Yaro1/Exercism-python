str_lower = "abcdefghijklmnopqrstuvwxyz"
str_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_ = [str_lower, str_upper]


def rotate(text, key):
    return ''.join([str_[i.isupper()][(str_lower.find(i.lower()) + key) % 26] if i.isalpha() else i for i in text])