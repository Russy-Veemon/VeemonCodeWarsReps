# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on: make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.

def solve(s):
    upper = 0
    lower = 0
    for x in s:
        if x.isupper():
            upper += 1
        else:
            lower += 1
    if upper > lower:
        return s.upper()
    else:
        return s.lower()