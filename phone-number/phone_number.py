import re


class PhoneNumber:
    def __init__(self, number):
        self.number = ''.join(filter(lambda x: x.isdigit(), number))
        if len(self.number) > 11 or (len(self.number) == 11 and self.number[0] != "1") or len(self.number) < 10:
            raise ValueError("Numbers too match.")
        self.number = self.number if len(self.number) == 10 else self.number[1:]
        if int(self.number[0]) < 2 or int(self.number[3]) < 2:
            raise ValueError("Numbers not enough")
        self.area_code = self.number[:3]

    def pretty(self):
        return '-'.join(["("+self.area_code+")", self.number[3:6], self.number[6:]])