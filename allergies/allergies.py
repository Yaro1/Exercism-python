"""
This is not my solution.
It was written for training.
"""


class Allergies:

    allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

    def __init__(self, score):
        self.score = score % 256

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        selected = []
        for index, value in enumerate(self.allergies):
            if self.score & 2 ** index:
                selected.append(value)

        return selected
