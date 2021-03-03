ENGLISH = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "elven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

MAGNITUDES = [
    None,
    "thousand",
    "million",
    "billion"
]


def say(number):
    joiner = " "
    if number < 0:
        raise ValueError("Can't deal with this negativity")
    elif number in ENGLISH:
        return ENGLISH[number]
    elif number < 100:
        joiner = "-"
        upper, lower = divmod(number, 10)
        parts = [say(upper * 10), say(lower)]
    elif number < 1000:
        upper, lower = divmod(number, 100)
        parts = [say(upper), "hundred", lower > 0 and say(lower)]
    else:
        triplets = split_into_triplets(number)
        parts = reversed([
            [say(triplet), say_magnitude(index)]
            for index, triplet in enumerate(triplets)
            if triplet > 0
        ])
    return joiner.join(flatten(parts))


def say_magnitude(magnitude_index):
    try:
        return MAGNITUDES[magnitude_index]
    except IndexError:
        raise ValueError("Can't deal with this magnitude")


def split_into_triplets(number):
    """
    Split a number into groups of three digits starting at the lower end
    """
    while number > 0:
        number, triplet = divmod(number, 1000)
        yield triplet


def flatten(phrases):
    """
    Flatten the list of phrases, filter out Nones/Falses at every level
    """
    def listify(list_or_not):
        return list_or_not if type(list_or_not) == list else [list_or_not]

    return [
        word
        for phrase in phrases if phrase
        for word in listify(phrase) if word
    ]