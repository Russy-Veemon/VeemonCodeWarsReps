# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
# For example, when the input is green, output should be yellow.

def update_light(current):
    if current == 'green':
        return 'yellow'
    if current == 'yellow':
        return 'red'
    if current == 'red':
        return 'green'

# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    result = ''
    for x in s:
        if x.isupper():
            result += " " + x
        else:
            result += x
    return result

# In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

def reverse_list(l):
    return l[::-1]

# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

def comp(a, b):
    if a is None or b is None:
        return False
    elif len(a) != len(b):
        return False
    else:
        a_squared = [i ** 2 for i in a]
        a_squared.sort()
        b.sort()
        return a_squared == b

# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

def check(array, thing):
    if thing in array:
        return True
    else:
        return False

# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

def problem(a):
    if isinstance(a, str):
        return "Error"
    else:
        return (a * 50) + 6

# Description:
# Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
# Examples
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
# remove("!Hi!") == "!Hi"
# remove("Hi! Hi!") == "Hi! Hi"
# remove("Hi") == "Hi"

def remove(s):
    if s.endswith("!"):
        return s[:-1]
    else:
        return s

# Task
# Given a string str, reverse it and omit all non-alphabetic characters.
# Example
# For str = "krishan", the output should be "nahsirk".
# For str = "ultr53o?n", the output should be "nortlu".
# Input/Output
# [input] string str
# A string consists of lowercase latin letters, digits and symbols.
# [output] a string

def reverse_letter(string):
    return ''.join(filter(str.isalpha, string))[::-1]
    #filter method used to find alphabete only, by asking
    #for str>>type of variable>> str.isalpha alphabet only
    #(x, string) to ask for the variable being passed
    #[::-1] to have the string returned backwards