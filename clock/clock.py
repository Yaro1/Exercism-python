def fill_nil(a):
    return a if len(a) > 1 else '0'+a


class Clock:
    def __init__(self, hour, minute):
        hour = hour % 24 if hour >= 0 else hour % 24 + 24
        self.minute = hour * 60 + minute

    def __repr__(self):
        h = fill_nil(str((self.minute // 60) % 24))
        m = fill_nil(str(self.minute % 60))
        return ':'.join([h, m])

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        self.minute += minutes
        return self.__repr__()

    def __sub__(self, minutes):
        self.minute -= minutes
        return self.__repr__()