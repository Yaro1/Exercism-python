"""
Try to understand not my solution.
"""

import calendar

day_dict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}


def meetup(year, month, week, day_of_week):
    data_class = calendar.Calendar()
    days = [d for d in data_class.itermonthdates(year, month) if
            d.weekday() == day_dict[day_of_week] and d.month == month]
    if week == "teenth":
        return [d for d in days if 13 <= d.day <= 19][0]
    elif week == "last":
        return days[-1]
    else:
        try:
            return days[int(week[0]) - 1]
        except IndexError:
            raise MeetupDayException("Error")


class MeetupDayException(Exception):
    def __init__(self, *args):
        super().__init__(args)
