from random import randint


def all_same_three(items):
    return all(x == items[0] for x in items) and len(items) == 3


def one_three_five(items):
    if 1 in items and 3 in items and 5 in items:
        return True
    return False


def two_four_six(items):
    if 2 in items and 4 in items and 6 in items:
        return True
    return False


def count_ones_and_fives(items):
    count = 0
    for item in items:
        if item == 5 or item == 1:
            count += 1
    return count


def consecutive(items):
    if 1 in items and 2 in items and 3 in items:
        return True
    elif 2 in items and 3 in items and 4 in items:
        return True
    elif 3 in items and 4 in items and 5 in items:
        return True
    elif 4 in items and 5 in items and 6 in items:
        return True
    else:
        return False
