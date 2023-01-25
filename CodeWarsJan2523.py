# Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates).

def min_value(digits):
    new_num = list(set(digits))
    new_num.sort()
    return int("".join(map(str, new_num)))