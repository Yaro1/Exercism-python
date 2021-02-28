from collections import Counter


def find_anagrams(word, candidates):
    word_counter = Counter(word.lower())
    return [i for i in candidates if Counter(i.lower()) == word_counter and word.lower() != i.lower()]
