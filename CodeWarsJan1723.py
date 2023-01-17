# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

def correct(s):
    s = s.replace("5", "S")
    s = s.replace("0", "O")
    s = s.replace("1", "I")
    return s

# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
# Example: (Input1, Input2 -->Output)
# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"

def sum_str(a, b):
    if a == '':
        a += '0'
    if b == "":
        b += '0'
    return str(int(a)+int(b))

# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.
# For example:
# a = 1
# b = 4
# --> [1, 2, 3, 4]

def between(a,b):
    array = []
    for x in range (a, b+1):
        array.append(x)
    return array

# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    return s.replace('!', "")