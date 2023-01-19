# Can you find the needle in the haystack?
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:

def find_needle(haystack):
    for x in haystack:
        if x == "needle":
            return "found the needle at position " + str(haystack.index(x))

# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)