# Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.
# Division by zero should return an empty value.

def remainder(a,b):
    if min(a,b) == 0:
        return None
    elif a > b:
        return a % b
    else: 
        return b % a
    
# You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.
# Find max(abs(length(x) − length(y)))
# If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

def mxdiflg(a1, a2):
    if a1 == []  or a2 == []:
        return -1
    else:
        max_diff = -1
        for x in a1:
            for y in a2:
                diff = abs(len(x) - len(y))
                max_diff = max(max_diff, diff)
        return max_diff