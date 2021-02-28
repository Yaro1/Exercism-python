import re


def response(hey_bob):
    ans = re.sub("[^a-zA-Z123456789?]+", '', hey_bob)
    ans_letters = re.sub("[^a-zA-Z]+", '', hey_bob)
    if not ans:
        return "Fine. Be that way!"
    if hey_bob.upper() == hey_bob and ans_letters != "" and "?" == hey_bob.replace(' ', '')[-1]:
        return "Calm down, I know what I'm doing!"
    if "?" == hey_bob.replace(' ', '')[-1]:
        return "Sure."
    if hey_bob.upper() == hey_bob and ans_letters != "":
        return "Whoa, chill out!"
    return "Whatever."
