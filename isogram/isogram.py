def is_isogram(string):
    string = str.lower(string.replace(' ','').replace('-', ''))
    if sum(string.find(i, ind+1) != -1 for i, ind in zip(string, range(len(string) - 1))) > 0:
        return False
    return True