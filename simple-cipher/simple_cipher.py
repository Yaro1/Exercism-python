"""
I didn't like this tests.
Cause as we see they want that length of the key
in RandomKeyCipherTest should be equal or bigger than text.
why? :(

And as i saw at the peoples solving, i should use "from itertools import cycle".
"""

import random
from string import ascii_lowercase as symbols
from itertools import cycle


class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join([random.choice(symbols) for i in range(10)])
        else:
            self.key = key

    def encode(self, text):
        return ''.join([symbols[(ord(i) % 97 + ord(j) % 97) % 26] for i, j in zip(text, cycle(self.key))])

    def decode(self, text):
        return ''.join([symbols[(ord(i) % 97 - ord(j) % 97) % 26] for i, j in zip(text, cycle(self.key))])
