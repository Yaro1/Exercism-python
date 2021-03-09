SUBLIST = (lambda x, y: x in y)
SUPERLIST = (lambda x, y: SUBLIST(y, x))
EQUAL = (lambda x, y: len(x) == len(y) and SUBLIST(x, y))
UNEQUAL = (lambda x, y: len(x) != len(y) or not SUBLIST(x, y))

check_list = [EQUAL, SUBLIST, SUPERLIST, UNEQUAL]


def sublist(list_one, list_two):
    s1_ = ','.join([str(i) for i in list_one]) if list_one else ""
    s2_ = ','.join([str(i) for i in list_two]) if list_two else ""
    l_check = [i(s1_, s2_) for i in check_list]
    return check_list[l_check.index(True)]