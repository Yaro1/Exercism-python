import re


class PhoneNumber(object):
    _pattern = re.compile(r'''
        ^\+?1?              # optional literal `+` and country code
        (?:[-. ]+)?         # optional separators
        \(?([2-9]\d{2})\)?  # the area code, with or without surrounding parens
        (?:[-. ]+)?         # optional separators
        ([2-9]\d{2})        # the exchange code
        (?:[-. ]+)?         # optional separators
        (\d{4})$            # the subscriber number
    ''', re.VERBOSE)

    def __init__(self, phone_number):
        try:
            self.area_code, self.exchange, self.subscriber = \
                    self._pattern.search(phone_number.strip()).groups()
        except AttributeError:
            raise ValueError('Invalid `phone_number`')

    @property
    def number(self):
        return self.area_code + self.exchange + self.subscriber

    def pretty(self):
        return '({})-{}-{}'.format(self.area_code, self.exchange, self.subscriber)