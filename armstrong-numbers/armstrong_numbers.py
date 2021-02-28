def is_armstrong_number(number):
    length = len(str(number))
    return number == sum(int(i)**length for i in str(number))
