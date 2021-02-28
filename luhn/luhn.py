class Luhn:
    def __init__(self, card_num):
        str_ = ''.join(card_num.split())[::-1]
        if not str_.isdigit():
            self.flag = False
            return
        ans = 0
        for i, num in zip(str_, range(len(str_))):
            if num % 2:
               ans += int(i) * 2 if int(i) * 2 <= 9 else int(i) * 2 - 9
            else:
                ans += int(i)
        self.flag = str_.isdigit() and ans % 10 == 0 and len(str_) > 1

    def valid(self):
        return self.flag > 0


print(Luhn(":9").valid())
